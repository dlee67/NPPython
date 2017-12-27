# Write a prog, which accepts html, with the
# different http request, where the Accept-Language is requesting for Korean.

import urllib.request
import webbrowser
from urllib.request import Request

req = Request("https://www.google.com")
req.add_header("Accept-Language", "ko-kr")
response = urllib.request.urlopen(req)
webbrowser.open(response.url) # Thought every language aside from Korean will be filtered out, but it didn't.
 