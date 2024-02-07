f=open('text.txt','w')
f.write('hello all')
f=open('text.txt','r')
print(f.read())
l=['ravi','sunny','vsvs']
f=open('text.txt','a')
f.writelines(l)
f=open('text.txt','r')
print(f.read())
f.close()
print(f.closed)
'''hello all
hello allravisunnyvsvs
True
>>> '''
