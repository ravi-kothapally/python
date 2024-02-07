a=input('word')
b=input('word')
c=input('word')
d=input('word')
e=input('word')
for i in (a,b,c,d,e):
    while len(i)<6:
        print(i,end='')
        i=input('<6 re-enter')
    print(i)    
        
