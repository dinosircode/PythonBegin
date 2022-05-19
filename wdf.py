import array as arr
def Sumno():
	o=0
	e=0
	a=arr.array('i',[15,20,2,3,6,11,14,13,9,7])
	for x in range(0,10):
		if(a[x]%2==0):
			e=e+a[x]
		else:
			o=o+a[x]
	print("Array is")
	print(a)
	print("Sum of all add numbers is:",o)
	print("Sum of all Even numbers is:",e)	


Sumno()