x=int(input('enter base(odd)'))
s=(x-1)//2
t=x
f=0
for i in range(x+s):
    for k in range(s):
        print('  ',end='')
    for j in range(t):
        print('* ',end='')
    print()
    if t<(2*x-1) and f==0:
        t=t+2
        s-=1
    else:
        f=1
        s+=1
        t=t-2
        
        
        
    
              






