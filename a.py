def grade(s):
	if(s>=90):
		return "S"
	elif(s>=85)&(s<90):
		return "A+"
	elif(s>=80)&(s<85):
		return "A"
	elif(s>=75)&(s<80):
		return "B+"
	elif(s>=70)&(s<75):
		return "B"
	else:
		return "F"

a=int(input("Enter Marks"))
x=grade(a)
print(x)