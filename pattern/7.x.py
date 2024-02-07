x=int(input("even"))
for i in range(0,x):
    for j in range(0,x):
        if(j==i or j==x-i-1):
            print("*",end="")
        else :
            print(" ",end="")
    print("")        
