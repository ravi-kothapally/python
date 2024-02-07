class person:
    def __init__(self,n):
        self.n=n

    def greet(self):
        print('good morning',self.n)

o=person('ravi')
o.greet()
