x=int(input('enter num'))
for i in range (2*x+3):
    j=0
    while j<x+2:
        if i==0 or i==x+1 or i==2*x+2:
            print('  ',end='')
            while j<x:
                j+=1
                print("* ",end='')
        else:
            if j==0 or j==x+1:
                print('* ',end='')
            else:
                print("  ",end='')
        j+=1        
    print('')            
