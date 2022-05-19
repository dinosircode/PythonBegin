def fizzbizz(a):
	if(a%3==0):
		if(a%5==0):
			return ("Fizz Bizz")
		else:
			return("Fizz")
	else:
		if(a%5==0):
			return("Bizz")
		else:
			return(a)

a=int(input("Enter the Number"))
b=fizzbizz(a)
print(b)

