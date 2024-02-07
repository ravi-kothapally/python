x=0
p=n=z=0
while(x!=-1):
    x=int(input('enter number'))
    if x>0:
        p+=1
    elif x<0:
        n+=1
    else:
        z+=1
print('count of negative numbers=',n-1)
print('count of positive numbers=',p)
print('count of zeros=',z)
