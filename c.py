def funpriday(x):
	if(x==1):
		print("Sunday")
	elif(x==2):
		print("Monday")
	elif(x==3):
		print("Tuesday")
	elif(x==4):
		print("Wendsday")
	elif(x==5):
		print("Thurday")
	elif(x==6):
		print("Friday")
	elif(x==7):
		print("Saturday")
	else:
		print("Enter Valid Number Between 1-7")

a=int(input("Enter a Valid Input Between 1-7"))
funpriday(a)