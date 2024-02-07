x=float(input('enter three sides of triangle'));y=float(input());z=float(input())
if(x>0 and y>0 and z>0) and(x<y+z or y<x+z or z< x+y):
    s=(x+y+z)/2
    a=(s*(s-x)*(s-y)*(s-z))**0.5
    print('area of the triangle is',a)
else:
    print('side length should be positive\n sum of two side should be greater than third side')











