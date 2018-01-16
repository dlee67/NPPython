import urllib.request
import webbrowser
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import json
import paramiko
import socket
import ipaddress as ip
from urllib.request import Request
from urllib.request import build_opener, HTTPCookieProcessor
from http.cookiejar import CookieJar
from urllib.parse import urlparse
from urllib.parse import urljoin, parse_qs
from urllib.parse import quote
from urllib.parse import urlencode
from urllib.parse import urlunparse 

cookie_jar = CookieJar() # Place to store cookies...
# build_opener returns an instance of OpenerDirector, which is 
# 
#
opener = build_opener(HTTPCookieProcessor(cookie_jar))

opener.open('http://www.github.com')
print(len(cookie_jar)) # Length of my cookie

cookie = list(cookie_jar)
print(cookie)

print(cookie[0].secure)

print("Wanna compare kamehamehas?=======================================")
req=Request('https://www.gmail.com')
response=urllib.request.urlopen(req)
print(response.url)
#webbrowser.open(response.url)
print(req.redirect_dict)
print("Wanna compare kamehamehas?========================================")
result = urlparse("https://www.python.org/dev/peps")
print(result)
result = urlparse("http://www.python.org:8080/")
print(result)
result = urlparse("http://www.python.org")
print(result) #By default, since, no path has been specified in the urlparse,
			  #root path will be given.
result = urlparse("../images/tux.png")
print(result) #I can notice that netloc is not specified, that's because
			  #I am using the relative URL.
result=urljoin("http://www.debian.org", "intro/about")
print(result)
result=urlparse('http://docs.python.org/3/search.html? q=urlparse&area=default')
parse_qs(result.query)
print(result)
print(quote("A duck?"))
path='pypi'
path_enc=quote(path)
query_dict={':action': 'search', 'term:': 'Are you quite sure this is a cheese shop?'}
query_enc=urlencode(query_dict)
netloc="pypi.python.org"
urlunparse(('http', netloc, path_enc, '', query_enc, ''))
print(query_enc)
print("Wanna compare kamehamehas?========================================")
req=Request('http://www.google.com', method='HEAD')
response=urllib.request.urlopen(req)
print(response.status)
print(response.read())
#Well, I know a project to do now.
#Enable this code to open a webpage with Python in the search.
data_dict={'P': 'Python'}
data=urlencode(data_dict).encode('utf-8')
req=Request('http://search.debian.org/cgi-bin/omega', data)
req.add_header('Content-Type', 'application/x-www-form-urlencode;  charset=UTF-8')
response = urllib.request.urlopen(req)
someFile = open("openThis.html", "w+")
someFile.write(response.read().decode("utf-8"))
someFile.close()
print("Wanna compare kamehamehas?=============================")
root = ET.Element('inventory')
cheese=ET.Element('cheese')
cheese.attrib['id'] = 'c01'
name=ET.SubElement(cheese, 'name')
name.text='Caerphilly'
root.append(cheese)
ET.dump(root)
print(minidom.parseString(ET.tostring(root)).toprettyxml())
print("Wanna comapre kamehamehas?=============================")
l = ['a', 'b', 'c']
print(json.dumps(l))
print("Wanna compare kamehamehas?=============================")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#print(socket.gethostname()) #SICK.
#print(socket.gethostbyname(socket.gethostname()))
net4=ip.ip_network('10.0.1.0/24')
print(net4.netmask)
all_hosts=list(net4.hosts())
print(net4.supernet())