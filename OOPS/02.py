class employee:
    ''' am an emp'''
    def __init__(self,name,age,salary): # constructor
    #it is for defining all the class variables
        self.nko=name
        self.a=age
        self.s=salary
    def dis(self):
        print(self.nko)
        print(self.a)
        print(self.s)
emp1=employee('ravi',22,100000)
emp2=employee('jaswa',22,40000)
print(emp1.dis())
print(emp2.dis())
    
