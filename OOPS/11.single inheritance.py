class c:
    d=0
    def __init__(self,v):
        self.v=v
        c.d+=1
    def show(self):
        print(self.v)
        print(c.d)
class d(c):
    def __init__(self,v,n):
        c.__init__(self,v)
        self.n=n
    def sho(self):
        print(self.v,self.n)
o=d(5,'tavi')
print(o.v)
print(o.n)
p=d(6)
print(p.v)
print(p.n)
