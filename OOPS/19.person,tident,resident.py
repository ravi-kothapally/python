class person:
    def __init__(self,n,a):
        self.n=n
        self.a=a
    def name(self):
        return self.n
    def age(self):
        return self.a
class student:
    def __init__(self,i):
        self.i=i
    def id(self):
        return self.i
class resident(person,student):
    def __init__(self,n,a,i,place):
        person.__init(self,n,a)
        student.__init(self,i)
        self.p=place
    def sho(self):
        print(self.n,self.a,self.i,self,p)
o=resident('rai',20,151348,'uegycuegy')
