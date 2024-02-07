l=[]

s=0
x=int(input('no of elements'))
for i in range(x):
    g=int(input('enter number'))
    l.append(g)
print(l)
i=0
while(i<x):
    s=s+l[i]
    i+=1
print('sum of numbers=',s)
    
    
