def sumofn(x):
	sum=0
	for x in range(0,x):
		a=int(input("Enter the Number"))
		sum=sum+a
	return sum


a=int(input("Enter the number of numbers..:"))
b=sumofn(a)
print("Sum is :",b)