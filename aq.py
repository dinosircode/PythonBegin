def fibono(limit):
    a=0
    b=1
    print(a)
    print(b)
    for x in range(2,limit):
        c=a+b
        print(c)
        a=b
        b=c

e=int(input("Enter No of Terms"))
fibono(e)
