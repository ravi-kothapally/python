x=int(input("enter odd number"))

for i in range(0,x):
    for j in range (0,x):
        if i==x//2:
            print("* ",end="")
            continue
        elif j==x//2:
            print("* ",end="")
        else:
            print("  ",end="")
    print("")        
