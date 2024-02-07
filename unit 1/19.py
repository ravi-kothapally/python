x=int(input('enter number'))
c=0
s=0
while x!=0:
    s=s+x%10
    x=x//10
    c+=1
print(s)    
