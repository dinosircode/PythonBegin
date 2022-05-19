def asprint(limit):
	print("In Accending Order")
	for x in range(0,limit+1):
		print(x)
		

def dsprint(limit):
	print("In Descending Order")
	for x in range(limit,-1,-1):
		print(x)

x=int(input("Enter the Limit"))
asprint(x)
dsprint(x)
