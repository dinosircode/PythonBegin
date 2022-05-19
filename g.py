def printlist():
	print("")
	print("Rammu Stores..")
	print("_______________________________________________")
	print("| Item Number	|	Item	| Cost Per Item |")
	print("-----------------------------------------------")
	print(" 1	        |	banana	|	10")
	print(" 2	        |	apple	|	30")
	print(" 3 	        |	orange	|	25")
	print(" 4	        |	lemon	|	35")
	print("-------------------------------------------------")
 

def costofper(x):
	if(x==1):
		return 10
	elif(x==2):
		return 30
	elif(x==3):
		return 25
	elif(x==4):
		return 35
	else:
		return 0


def itemselect(x):
	if(x==1):
		return "banana"
	elif(x==2):
		return "apple"
	elif(x==3):
		return "orange"
	elif(x==4):
		return "lemon"
	else:
		return 0


def calccost(a,b):
	print("---------------------------------------------")
	print("Total Cost is:",a*b)

def selectitem():
	print("")
	print("Enter Item Number:")
	a=int(input(""))
	b=costofper(a)
	c=itemselect(a)
	print("-----------------------------------------------------")
	print("Item Selected :",c)
	print("-----------------------------------------------------")
	print("Cost Per Selected Item is:",b)
	print("-----------------------------------------------------")
	print("Enter No of Quantity:")
	qu=int(input(""))
	calccost(qu,b)


def thankyouslip():
	print("")
	print("--------------------------------------------------------")
	print("Thankyou for Shoping With Ramu Stores.. ")
	print("Visit Again...")
	print("----------------------------------------------------------")

printlist()
selectitem()
thankyouslip()