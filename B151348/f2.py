x=0
c=p=0
cu=0
while(x!=-1):
    cu=0
    x=int(input('enter  positive integer'))
    if x>0:
        for i in range(1,x+1):
            if(x%i)==0:
                cu+=1        
        if cu==2:
            p+=1
        else:
            if(x!=1):
                c+=1
    else:
         print('naturals only')
print('count of primes=',p)
print('count of composites=',c-1)
        
