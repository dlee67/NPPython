import urllib.request

rfc_number = input("Enter the RFC number: ");

try:
	byte_stream = urllib.request.urlopen("http://www.ietf.org/rfc/rfc" + rfc_number + ".txt").read()
	decoded_stream = byte_stream.decode()
except urllib.error.HTTPError as e:
	print("Status code: ", e.code)
	print("Reason: ", e.reason)
	print("URL: ", e.url)
	
print(decoded_stream)