x=int(input("even num"))
for i in range(0,x//2):
    for j in range(0,x-2*i):
        print("* ",end="")
    print("")    
    for k in range(0,i+1):
        if(i==x//2-1 and k==i):
            print(" *",end="")
        else   :
            print("  ",end="")    
        
        
