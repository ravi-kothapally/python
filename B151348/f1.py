c=6
for i in range(0,c):
    x=input('enter string')
    print(i)
    if len(x)<6:
        i-=1
        print(i)
        print('enter again')
    else:
        print(x)
         
