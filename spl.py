def Quadfinder(x,y):
    if (x==0):
        if(y==0):
            return "Orgin "
        elif(y>0):
            return "On Y +ve Axis"
        else:
            return "On Y -ve Axis "
    elif(x>0):
        if(y==0):
            return "On Positive X Axis"
        elif(y>0):
            return "1 St Quadrient"
        else:
            return "4th Quadrent"
    else:
        if(y==0):
            return "On Negative X Axis"
        elif(y>0):
            return "2nd Quadrent"
        else:
            return "3rd Quadrent"

a=int(input("Enter X axis:"))
b=int (input("Enter Y axis:"))
c=Quadfinder(a,b)
print(c)
