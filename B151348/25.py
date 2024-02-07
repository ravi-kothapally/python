x=float(input('initial investment'))
i=float(input('annual interest'))
t=int(input('years'))
yearly_interest=x*i/100
h=yearly_interest
for i in range(t):
    x=x+h
print(x,' is investment amount')    
