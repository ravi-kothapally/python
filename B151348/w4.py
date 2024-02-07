e=0
o=0
ce=0
co=0
while 1:
    x=int(input("enter num"))
    if(x>=0):
        
        if x%2==0:
            ce+=1
            e=e+x
        else:
            co+=1
            o=o+x
    elif x!=-1:
         print('enter naturals only')
    else:
        break
if(ce!=0):
    print(" even\nsum = ",e,"  avg=",e/ce,"  count=",ce,)
else:
    print('no evens')
if(co!=0):    
    print("odd\n sum =",o, "  avg=",o/co," count=",co,)
else:
    print('no odds')
         
        
