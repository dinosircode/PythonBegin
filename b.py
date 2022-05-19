def taxrate(x):
	if(x>=10000000):
		y=int((15*x)/100)
		return y 
	elif(x>=5000000)&(x<10000000):
		y=int((10*x)/100)
		return y
	elif(x>=100000)&(x<5000000):
		y=int((8*x)/100)
		return y
	else:
		y=int((6*x)/100)
		return y

a=int(input("Enter Price"))
c=taxrate(a)
print("Price of Car:",a)
print("Tax Rate :",c)
print("Total Price:",a+c)