import urllib.request

rfc_number = input("Enter the RFC number: ");

byte_stream = urllib.request.urlopen("http://www.ietf.org/rfc/rfc" + rfc_number + ".txt").read()
decoded_stream = byte_stream.decode()

print(decoded_stream)