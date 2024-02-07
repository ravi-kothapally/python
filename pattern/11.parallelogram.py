x=int(input('num'))
for i in range(0,x):
    for k in range(0,i):
        print(" ",end="")
    for j in range(0,x):
        if i==0 or i==x-1:
            print("* ",end="")
        else:    
            if(j==0 or j==x-1):
                print("* ",end="")
            else:
                print("  ",end="")
    print("")     
            
