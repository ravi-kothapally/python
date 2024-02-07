x=(input('enter something'))
if(ord(x)>47 and ord(x)<57):
    print('digit')
elif(ord(x)>=65 and ord(x)<=91) or(ord(x)>=97 and ord(x)<=122):
    print('alphabet')
elif(ord(x)==32):
    print('space')
else:
    print('not aplhabet not space not digit')
    
