'''
f=open('f1.txt','r')
c=f.read()
c=c.replace('ravi','sunny')
f=open('f1.txt','w')
print(c)
f.write(c)
f.close()
output:
sunny is the good boy of the class.sunny is the tallest of all the class mates.sunny hates sunny.sunny loves sunny.


f=open('f1.txt','r')
c=f.read()
c=c.split('a')
f=open('f1.txt','w')
print(c)
f.close()

ouput:
['sunny is the good boy of the cl', 'ss.sunny is the t', 'llest of ', 'll the cl', 'ss m', 'tes.sunny h', 'tes sunny.sunny loves sunny.']

'''
