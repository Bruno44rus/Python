import urllib.request
import requests
import io
import re
url1 ='http://evil.bigazzzz.ru:15073/test.html'
'''page = urllib.request.urlopen(url1)
page1 = str(page.read().decode('utf-8'))
file = open("file1.txt", "w")
file.write(page1)
file.close()'''


def emails(text):
    pattern = r'[A-Za-z0-9+%-.]+@[A-Za-z0-9-.]+\.[A-Za-z]'
    return set(re.findall(pattern,text))


def links(text):
    bad_result = set()
    pattern = r'href="(.+)"'
    bad_urls = [
        'mailto:(.+)',
        'tel:(.+)',
        'javascript:(.*)',
        '#(.*)'
    ]
    urls = set(re.findall(pattern,text))
    for url in urls:
        for bad_url in bad_urls :
            if re.fullmatch(bad_url, url)!=None:
                bad_result.add(url)
    return urls - bad_result


'''def forms(text):
    m = set()
    index = 0
    while text.find(r'<form(.+)>', index) >=0:
        start_tag_form = text.find(r'<form(.+)>')
        form_len = len(text.find(r'<form(.+)>'))
        start = start_tag_form + form_len
        end = text.find(r'</form>',start)
        m += text[start:end]
        index = end
    return m'''


html_response = requests.request('GET', url1)
print(links(html_response.text))
print(emails(html_response.text))
#print(forms(html_response.text))

text = html_response.text
m = set()
index = 0
while text.find(r'<form', index) >= 0:
    start_tag_form = text.find(r'<form', index)
    end_tag_form = text.find('>',start_tag_form)
    form = text[start_tag_form:end_tag_form]
    form_len = len(form)
    start = start_tag_form + form_len
    end = text.find('</form>',start)
    print(text[start_tag_form:end+7])
    index = end



