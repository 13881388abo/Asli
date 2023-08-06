def bmm(x,y):
    n = z = 0
    if abs(x)>abs(y):
        n = abs(x)
    else:
        n = abs(y)
    for i in range(1,n+1):
        if x%i==0 and y%i==0:
            z=i
            print("khoroojiz",z)
    return(z)

x = int(input("please enter x:"))
Y = int(input("please enter y:"))
javab = bmm(x,Y)
print(javab)