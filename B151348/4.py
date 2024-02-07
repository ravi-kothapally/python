x=int(input('enter quantity'))
y=float(input('enter value of each'))
z=float(input('discoun%='))
if(x>0 and y>0 and z>=0):
    s=y-(y*z)/100
    print('total amount=',s*x)
else:
    print('quantity,value should be greater than zero')
    print('discount should not be negative')
