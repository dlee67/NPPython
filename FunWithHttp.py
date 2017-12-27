# Write a prog, which accepts html, with the
# different http request, where the Accept-Language is requesting for Korean.

import urllib.request
import webbrowser
from urllib.request import Request

req = Request("https://www.naver.com/")
req.add_header("Accept-Charset", "ASCII")
response = urllib.request.urlopen(req)
print(response.read())
webbrowser.open(response.url) # Thought every language aside from English will be filtered out, but it didn't.
 