'''import filecmp
print(filecmp.cmp('f1.txt','text.txt'))


from shutil import copyfile as f
f('text.txt','f1.txt')
'''
f=open("f1.txt","r")
d=f.readlines()
mylist=[]
m=[]
mydict={}
for i in range(0,len(d)):
    print(d[i])
    mylist.extend(d[i].split())
for i in mylist:
    m.append((len(i),i))
    if i not in mydict.keys():
        mydict[i]=mylist.count(i)
print (max(m),"\n")
print (mydict)
'''
f=open('f1.txt','r')

#f.seek(3,0)
c=f.read()
print(c)
print(len(c))
f.close()
'''









