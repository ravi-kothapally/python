Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=[1,2]
>>> a.index(1)
0
>>> a.index(0)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.index(0)
ValueError: 0 is not in list
>>> a.index(1,2)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.index(1,2)
ValueError: 1 is not in list
>>> a.index(1)
0
>>> a.index(2)
1
>>> a.index(2,1)
1
>>> a.index(2,1)
1
>>> a.index(1,2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.index(1,2)
ValueError: 1 is not in list
>>> a=[1,1,2,3]
>>> a.count(1)
2
>>> a=[1,2,3]
>>> a.insert(1,5)
>>> a
[1, 5, 2, 3]
>>> a.sort()
>>> a
[1, 2, 3, 5]
>>> a.reverse()
>>> a
[5, 3, 2, 1]
>>> a.remove(5)
>>> a
[3, 2, 1]
>>> a.pop()
1
>>> a.pop(1)
2
>>> b=[3,4,5,6]
>>> a.extend(b)
>>> a
[3, 3, 4, 5, 6]
>>> a.insert(8,8)
>>> a
[3, 3, 4, 5, 6, 8]
>>> a.insert(100,45)
>>> a
[3, 3, 4, 5, 6, 8, 45]
>>> a.index(45)
6
>>> glue='7'
>>> glue.joint(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    glue.joint(a)
AttributeError: 'str' object has no attribute 'joint'
>>> glue=':'
>>> b=glue.joint(a)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    b=glue.joint(a)
AttributeError: 'str' object has no attribute 'joint'
>>> a="ravi"
>>> b=glue.joint(a)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b=glue.joint(a)
AttributeError: 'str' object has no attribute 'joint'
>>> b=\\glue.joint(a)
SyntaxError: unexpected character after line continuation character
>>> 
>>> 

>>> b=glue.join(a)
>>> b
'r:a:v:i'
>>> glue="leon"
>>> b=glue.join(a)
>>> b
'rleonaleonvleoni'
>>> a=[1,2,3,4,5]
>>> b=glue.join(a)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    b=glue.join(a)
TypeError: sequence item 0: expected str instance, int found
>>> a=['ravi','rgukt']
>>> b=glue.join(a)
>>> b
'ravileonrgukt'
>>> a=['ravi','sunny','rgukt']
>>> b=glue.join(a)
>>> b
'ravileonsunnyleonrgukt'
>>> 
>>> 


>>> 

>>> 


>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 
>>> 
>>> 
>>> 
