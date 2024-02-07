x=1
y=1
for i in range(6):
    for k in range(15-y):
        print(" ",end='')
    for j in range (x+2*i):
        print("8",end='')
    x=x+2*i
    y=y+i+1
    print("")    
          
