import array as arr
def result():
	a=arr.array('i',[19,20,19,2,19,3,2,34,5,4])
	n=0
	t=0
	for x in range(0,10):
		if(a[x]==19):
			n=n+1
		elif(a[x]==2):
			t=t+2
		else:
			pass

	if(n>=3):
		if(t>=2):
			print("True")
		else:
			print("False")

result()