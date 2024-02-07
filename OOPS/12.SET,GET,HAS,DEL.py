class c:
    d=0
    def __init__(self,v):
        self.v=v
        c.d+=1
    def show(self):
        print(self.v)
        print(c.d)
o=c(8)
print(hasattr(o,'v'))
print(hasattr(o,'a'))
print(getattr(o,'v'))
print(getattr(o,'a'))# make it a comment during execution
print(setattr(o,'v',9))
print(getattr(o,'v'))
print(setattr(o,'a',8))
print(delattr(o,'v'))
print(delattr(o,'a'))

