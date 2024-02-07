class student:                # class definition
    '''iam a student'''
    num=123                   # class variable
    def dis(self):            # class method
        ''' self :refering to itself'''
        print('my details')
# use '.' operater to acce the values of the class
stu1=student()                # object creation
print(student.num)
print(student.dis)
print(student.__doc__)
print(stu1.num)
print(stu1.dis)
print(stu1.dis())
