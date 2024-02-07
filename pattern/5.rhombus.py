x=int(input("odd num"))
z=1
y=x//2
for i in range(0,x):
    for k in range(0,y):
        print(" ",end="")
    for j in range(0,z):
        print("*",end="")
    print("")
    if(i<x//2):
        z=z+2
        y=y-1
    else:
        z=z-2
        y=y+1
        
        
