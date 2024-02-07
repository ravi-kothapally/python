class c:
    d=0
    def __init__(self,v):
        self.v=v
        c.d+=1
    def show(self):
        print(self.v)
        print(c.d)
o=c(5)
o.show()
p=c(6)
p.show()
q=c(8)
r=c(9)
t=c(88)
t.show()
print(c.d)
