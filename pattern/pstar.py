x=int(input("enter number"))
for i in range (x):
    for k in range(x-1-i):
        print(' ',end='')
    for j in range (2*i+1):
        if j%2==0:
            print('*',end='')
        else:
            print('p',end='') 
    print('')   
