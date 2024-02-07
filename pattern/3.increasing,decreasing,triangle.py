x=int(input("even no"))
for i in range(0,x//2):
    for j in range(0,i+1):
        print("* ",end="")
    if(i==(x//2)-1):        
        print("")
    else:
        print("\n")
for i in range(0,x//2):
    print("  ",end="")
    if(i==(x//2-1)):
        print("* ")
for i in range(x//2,0,-1):
    for j in range(0,i):
        print("* ",end="")
    if(i==1):        
        print("")
    else :      
        print("\n")     
    
