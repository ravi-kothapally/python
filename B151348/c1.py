sal=float(input('enter salary'))
gen=input('enter gender M/F')
ex=0
if( gen=='M'):
    di=sal*5/100
elif(gen=='F'):
    di=sal/10
if(sal<=10000):
    ex=sal*2/100
print('total salary after bonus=',sal+di+ex)    

  
        
