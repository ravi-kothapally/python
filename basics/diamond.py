x=int(input('enter size(odd)'))
for i in range(x):
    for j in range (x):
        if (i<=x//2 and( i+j<=x//2 or i<=j-x//2)) or i>x//2 and( i>=j+x//2 or i+j>=x//2*3):
            print('*',end="")
        else:
            print(' ',end='')
    print()
      
