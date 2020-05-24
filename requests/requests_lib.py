import requests


url = "https://thearjun.tech"
res = requests.get(url)

print(res.ok)
print(res.status_code)
print(res.headers)

# Returns the header items
print(res.headers.items())

# Formatting response headers
for key, value in res.headers.items():
    print(key, "    :    ", value)
