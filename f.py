def smallno(a,b,c):
	if(a<b):
		if(a<c):
			print(a,"is the Smallest")
		else:
			if(b<c):
				print(b,"Is small")
			else:
				print(c,"is Small")
	else:
		if(b>c):
			print(c,"is the Smallest")
		else:
			print(b,"is Smallest")

a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
c=int(input("Enter 3rd Number"))


smallno(a,b,c)