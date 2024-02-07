x='s'
d=l=u=0
print('-1 to exit')
while(x!='-1'):
    x=input('enter something')
    if(x>='0' and x<='9'):
        d+=1
    elif (x>='a' and x<='z'):
        l+=1
    elif(x>='A' and x<='Z'):
        u+=1
print('no of lower case letters=',l)
print('no of upper case letters=',u)
print('no of digits=',d)
