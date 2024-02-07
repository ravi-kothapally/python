x=float(input('enter 10th percentage'))
y=float(input('inter percentage'))
z=float(input('graduation percentage'))
if(x>80 and y>80 and z>70):
    print('you are eligible for pg')
    print('wanna change stream y/n')
    x=input()
    if(x=='y'):
        z=z-z/20
        if(z>70):
            print('eligible')
        else:
            print('not eligible')
    else:
         print('thank you')
else:
    print('not eligible for pg')
