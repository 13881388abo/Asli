def a ():
    c=int(input("toll safhe ra vared konid :    "))
    b=int(input("arz safhe ra vared konid :     "))
    for i in range(b):
        for j in range(c):
            if i%2==0 :
                if j%2==0:
                    print("#", end=" ")
                else :
                    print("*", end=" ")
            else:
                if j%2==0:
                    print("*", end=" ")
                else:
                    print("#", end=" ")
        print()
a()