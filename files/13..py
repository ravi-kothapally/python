f=open("f1.txt",'r')
f2=open("x.txt",'w')
fl=f.readlines()
c=0
for i in fl:
    c=c+1
    if c==4 and 'good' in i:
        m=[]
        m.extend(i.split())
        d=m.index('good')+1
        m.insert(d,'morning')
        i=' '.join(m)
        i=i+'\n'
    f2.write(i)
f.close()
f2.close()
        
        
    
