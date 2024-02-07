'''with open('f1.txt','r') as f:
    for i in f:
        print(i)
print(f.closed)

f=open('f1.txt','r')
for i in f:
    print(i)
'''
f=open('f1.txt','r')
print(f.tell())
#data=f.read()
#data=data.replace('#',' ')
#print(data)
print(f.readline(-1))
(f.seek(6))
print(f.tell())
print(f.read())
print(f.tell())
