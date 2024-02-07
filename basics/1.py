j=50
for i in range(1,j):
    c=0
    for k in range(1,i):
        if i%k==0:
           c+=1
    if c==2:
        print(i)
    
