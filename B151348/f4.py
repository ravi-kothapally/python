x=int(input("enter number x"))
y=int(input("enter number y"))
for i in range (0,y):
    for j in range (0,x):
        if i==0 or i==y-1:
            print("* ",end="")
            #print("")
            continue
        elif j==0 or j==x-1:
            print("* ",end="")
        else:
            print("  ",end="")

    print("")      
        
            
            
