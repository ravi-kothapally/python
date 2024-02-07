#.Write a python program to insert one line into an existing file as a 3rd line?
import os
f=open("f1.txt","r")
f2=open("n.txt","w") 
c=0
for line in f:
    c=c+1
    f2.write(line)
    if(c==2):
        f2.write("This is third line\n")
#os.remove("f1.txt")
#os.rename("n.txt","f1.txt")
f.close()
f2.close()

