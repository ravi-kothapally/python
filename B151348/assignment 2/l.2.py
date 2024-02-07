'''
l=[]
s=0
x=int(input('no of elements'))
for i in range(x):
    g=int(input('enter number'))
    l.append(g)
print(l)
i=0
while(i<x):
    if(l[i]%2==0):
        s=s+l[i]
    i+=1
print('sum of numbers=',s)

#l3
l=[]
c=[]
l=input('enter list')
print(l)
i=0
while(x-1>-1):
    c.append(l[x-1])
    x-=1
    i+=1
print('reversed list is',c)
    
#l4    
l=[]
f=1
l=input('enter list')
print(l)
e=input('enter search element')
for i in range(len(l)):
    if e==l[i]:
        print('found')
        f=1
        break
    else:
        f=0
if(f==0):
    print('not found')


#5
c=0
l=[]
l=input('enter list')
x=input('element to be counted')
for i in range(len(l)):
    if l[i]==x:
        c+=1
print('if found',c,'times')



#6
l=[]
for i in range(51):
    if i%3==0 or i%6==0:
        l.append(i)
print('list is',l)
'''
#l7
l=[]
s=0
x=int(input('no of elements>10'))
for i in range(x):
    g=int(input('enter number'))
    l.append(g)
#a
print(l)
#b
print(x)
#c
print(l[0],l[x-1])
print(l[-1],l[-2])
#d
#e
print(l[-3:])
#f
print(l[:-3])
#g
y=int(input('new element'))
i=int(input('index'))
l[i]=y
print('updated list',l)
#h
l[2:5]=[100]
#i
print(l)
print('length=',len(l))



    
        






