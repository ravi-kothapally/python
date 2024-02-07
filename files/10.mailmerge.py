n=open('names.txt','r')
b=open('body.txt','r')

x=b.read()
for i in n:
    c=i+x
    f=open(i.strip()+'.txt','w')
    f.write(c)
    f.close()
n.close()
b.close()
