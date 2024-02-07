'''
import sys
i=0
while 1:
    try:
        x=int(input('enter'))
        r=1/x
        break
    except check as e:
        print(sys.exc_info()[0])
print(r)
'''
class Check(Exception):
    def __init__ (self,data):
        self.d=data
    def __str__ (self):
        return repr(self.d)
try:
    raise Check(200)
except Check as r:
    print(r.__str__())
