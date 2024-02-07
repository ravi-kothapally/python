x=int(input("num"))
z=1
y=x
for i in range(0,2*x-1):
    for k in range(0,z):
        print(" ",end="")
    for j in range(0,y):
        print("*",end="")
    print("")
    if(i<x-1):
        z=z+1
        y=y-1
    else:
        z=z-1
        y=y+1
        
