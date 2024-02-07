x=input('enter string')
c='o'
while(c!='e'):
    c=input('do u want to repeat or concat or exit r/c/e')
    if(c=='r'):
        print('no of times')
        t=int(input())
        print(x*t)
    elif c=='c':
        y=input('enter string')
        print(x+y)
