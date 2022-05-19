def speed(a):
	c=0
	if a<=70:
		print("Speed Ok.!")
	else:
		b=a-70
		c=int(b/5)
		print("Total Demerits Points is",c)

	if (c>=12):
		print("License Suspended")


x=int(input("Enter Speed"))
speed(x)