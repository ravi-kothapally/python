x=int(input('num'))
for i in range(0,x):
    y=i+1
    for k in range(0,x-i):
        print(" ",end="")
    for j in range(0,i*2+1):
        print(y,end="")
        if(j<i):
            y+=1
        else:
            y-=1
    print("")
    
    
        
        
