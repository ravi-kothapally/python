x=int(input('basae(odd))'))
s=(x-1)//2
for i in range(x+s):
    for j in range(2*x-1):
        if i+j==s or i-s==j or i+x+s-1==j or i+j==2*x-2+s or(j>s and j<x+s and i==0):
            print('* ',end='')
        else:
            print('  ',end='')
    print()
