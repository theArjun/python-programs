import urllib.request

try:
    url = urllib.request.urlopen("https://www.thearjun.tech/")
    content = url.read()
    url.close()
except urllib.error.HTTPError:
    print("The web page is not found")
    exit()

# Write binary
f = open('thearjun.html', 'wb')
f.write(content)
f.close()
