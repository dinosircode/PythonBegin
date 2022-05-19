def vote(x):
	if(x>=18):
		print("Eligible to Vote")
	else:
		print("Not Eligible to Vote")

a=int(input("Enter the age"))
vote(a)