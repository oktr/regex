
import re

print("Regex teszt")
ipCim = input("Ip cím: ")

egyezes = re.match( "^[0-9]{,3}$", ipCim )

if( egyezes ):
	print("ok")
else:
	print("rossz")
	
