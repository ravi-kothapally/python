class person:
    def __init__(self,n,d):
        self.n=n
        self.d=d
    def age(self):
        print(self.n)
        print(2018-self.d)

o=person('ravi',1999)
o.age()
