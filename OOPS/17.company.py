class comp_mm:
    def __init__(self,name,designation,age):
        self.n=name
        self.d=designation
        self.a=age
    def sho(self):
        print(self.n)
        print(self.d)
class factory_staff(comp_mm):
    def __init__(self,n,d,a,oa):
        comp_mm.__init__(self,n,d,a)
        self.o=oa
    def sho(self):
        print(self.n)
        print(self.d)
        print(self.o)
class office_staff(comp_mm):
    def __init__(self,n,d,a,ta):
        comp_mm.__init__(self,n,d,a)
        self.t=ta
    def sho(self):
        print(self.n)
        print(self.d)
        print(self.t)
    
m1=factory_staff('ravi','fact',19,890)
m1.sho()
m2=comp_mm('fuii','rgvrgd',12)
m2.sho()
m3=office_staff('dfg','efgef',14,567)
m3.sho()
