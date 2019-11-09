import urllib.request
url1 ='http://evil.bigazzzz.ru:15073/test.html'
page = urllib.request.urlopen(url1)
page1 = str(page.read().decode('utf-8'))
file = open("file1.txt", "w")
file.write(page1)
file.close()
