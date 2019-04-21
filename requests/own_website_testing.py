import requests

r = requests.get('https://thearjun.tech')

# Prints the response object.
print(r)

# Prints the methods and documentation related to response object.
print(help(r))

# Prints text format of the response object.
print(r.text)

# Prints boolean data relating to response object.
print(r.ok)

# Prints the content of response object including image, audio, video.
print(r.content)

# Prints the HTTP status codes.
print(r.status_code)

# Prints the related headers file to response object.
print(r.headers)
