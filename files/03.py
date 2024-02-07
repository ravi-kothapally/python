f=open('text.txt','r+')# file opening
print(f.read())
print(f.name)
print(f.mode)
f.write('hello all')
f=open('text.txt','r+')
print(f.read())
l=['ravi','sunny','vsvs']
f.writelines(l)
f=open('text.txt','r+')
print(f.read())
f.close()
print(f.closed)
