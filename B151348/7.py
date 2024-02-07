p=float(input('enter principle rate per month and time in months'))
r=float(input())
t=int(input())
i=(p*t*r)/100
print('SI =',i,'total aount=',p+i)
c=p*((1 + r/100)**(t))
print('CI=',c)
              
