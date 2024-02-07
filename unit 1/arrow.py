x=int(input("enter height of arrow"))
y=int(input("enter height of rectangle"))
z=int(input("width odd"))       
a=x
b=1
for i in range (0,x+y):
    for k in range(a):
        print(" ",end="")
    for j in range (0,b):
        print("*",end="")
    print("")
    if(i<x):
        a-=1
        b+=2
    else:
        b=z
        a=(2*x+1-z)//2        
        
        
        
        
