def sumnumbers(limit):
	sum=0
	for x in range(0,limit+1):
		if(x%3==0):
			sum=sum+x
		else:
			if(x%5==0):
				sum=sum+x
	
	return sum

x=int(input("Enter the Limit"))
y=sumnumbers(x)
print(y)
