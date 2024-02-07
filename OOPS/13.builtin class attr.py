class c:
    'no name for the class'
    d=0
    def __init__(self,v):
        self.v=v
        c.d+=1
    def show(self):
        print(self.v)
        print(c.d)
    def __repr__(self):
        return 'no name'
    def __cmp__(self,other):
        return cmp(self,other)
o=c(8)
p=c(0)
print (o)
print(p)
print(c.__cmp__)
print(c.__doc__)
print(c.__name__)
print(c.__dict__)
print(c.__module__)
print(c.__bases__)

