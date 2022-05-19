def shownumbers(limit):
	for x in range(0,limit):
		if(x%2==0):
			print(x,"Even")
		else:
			print(x,"Add")

x=int(input("Enter the Limit"))
shownumbers(x)