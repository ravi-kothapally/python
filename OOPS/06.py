class person:
    c=0
    def __init__(self,n):
        self.n=n
        person.c+=1

    def greet(self):
        print('good morning',self.n)
o=person('ravi')
p=person('jess')
r=person('sunny')
e=person('parom')
d=person('gh')
print(person.c)

