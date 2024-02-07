c=int(input('enter max stars'))
x=c
for i in range(2*x-1):
    for j in range(c):
        if(j<=i):
            print('* ',end='')
            
    print('')
    if(i+1>=x):
        c-=1
    
