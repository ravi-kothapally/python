class Employee:
    num_of_emps=0
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first +'.'+last+'@gmail.com'
        Employee.num_of_emps+=1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay*Employee.raise_amount)
class Developer(Employee):#Inheriting the class called employee
    def __init__(self,first,last,pay,prog_lang):
        Employee.__init__(self,first,last,pay)#Inheriting all the variables from
        #employee(base)class
        self.prog_lang=prog_lang#And creating onemore instance variable called
#prog_lang in derived class called Developer
dev_1=Developer('a','b',50000,'python')
dev_2=Developer('c','d',60000,'java')
print(dev_1.email)
print(dev_2.prog_lang)
