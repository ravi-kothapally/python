e=0
o=0
ce=0
co=0
while 1:
    x=int(input("enter num"))
    if(x!=-1):
        if x%2==0:
            ce+=1
            e=e+x
        else:
             co+=1
             o=o+x
    else:
        break
print(" even\nsum = ",e,"  avg=",e/ce,"  count=",ce,)
print("odd\n sum =",o, "  avg=",o/co," count=",co,)
         
        
