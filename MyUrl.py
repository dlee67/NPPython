import sys, urllib.request

url = urllib.request.urlopen('https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen').read()
someOutput = url.decode()
print(someOutput)