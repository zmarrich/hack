#! /usr/bin/env python3
#team 73
#Zoe Marrich-Simon
print('Content-type: text/html\n')
import urllib.request
html = """

<html>
    <head><title>Crack It!</title></head>
    <body>
    <h1>Can you crack the PIN?</h1>
    <p> You tried: {pin} </p>

<p>{message}</p>
</html>
"""
int1=form.getfirst("num1","")
int2=form.getfirst("num2","")
int3=form.getfirst("num","")
int4=form.getfirst("num4","")
form = cgi.FieldStorage()
for i in range (70,79):
	groupnum =('{num:02d}'.format(num=i))
	for int1 in range(0,10):
		for int2 in range(0,10):
			for int3 in range(0,10):
				for int4 in range(0,10):
				try:
					url="http://cgi.soic.indiana.edu/~ebigalee/secret_vault.cgi?"
					url+="groupname={groupNum}&num1={int1}&num2={int2}&num3={int3}&num4={int4}"
					webpage=urllib.request+urlopen(url)
					lines= webpage.read().decode(errors="replace")
					webpage.close()
					#print lines
					if "Wrong!" not in lines:
						print("RIGHT!")
						print("Digit 1:", str(int1))
						print("Digit 2:", str(int2))
						print("Digit 3:", str(int3))
						print("Digit 4:", str(int4))
