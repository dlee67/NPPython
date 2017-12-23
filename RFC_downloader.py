import sys, urllib.request

try:
	#We've learned this in OS3600,
	#sys.argv is something that is passed onto the application that I'm running through a command prompt.
    rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
    print('Must supply an RFC number as first argument')
    sys.exit(2)

#template, in this program, is something that is waiting to be formatted.
template = 'http://www.ietf.org/rfc/rfc{}.txt'
url = template.format(rfc_number)

#urlopen() returns something that can be dealt by context manager, which is ...
#https://www.python.org/dev/peps/pep-0343/ <- explained there.
rfc_raw = urllib.request.urlopen(url).read()
#decode() is a in-built method, which could be invoked by a byte object, where decode() returns the string
#of decoded bytes.
#Remember? Everything in Python is data type.
rfc = rfc_raw.decode()
print(rfc)