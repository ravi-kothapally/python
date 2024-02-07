x='l'
n=o=0
print('-1 to stop')
while x!='-1':
    x=input('enter new or old ')
    if(x=='new'):
        n+=1
    elif x=='old':
        o+=1
print('total cost=',n*75+o*50)        
        
