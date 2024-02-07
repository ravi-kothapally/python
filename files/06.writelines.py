f=open('f1.txt','w')# file opening
l=['ravi','tavi','kavi']
print(f.write('ravi'))
print(f.writelines("comes"))
f.close()
print(f.closed)
