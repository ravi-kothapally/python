class student:
    def __init__(self,n,m):
        self.n=n
        self.m=m[0]
        self.v=m[1]
        self.b=m[2]
    def avg(self):
        print(self.n)
        self.avg=(self.m+self.v+self.b)/3
        print(self.avg)
li=[]
for i in range(3):
    o=input('enter object')
    n=input('name,3 test marks')
    m=[]
    for j in range(3):
        k=int(input('enter marks'))
        m.append(k)
    o=student(n,m)         
    li.append(o)
for i in li:
    i.avg()
    
