y=int(input("odd no"))
x=y//2+1
f=0
for i in range(0,y):
    for j in range(0,y):
        if i==0 or i==y-1:
            print("* ",end="")
        else:
            if(j<x or j>y-1-x):
                print("* ",end="")
            else:
                print("  ",end="")
    if(x!=1 and f==0):
        x=x-1
    else:
        f=1
        x=x+1
    print("")
 
