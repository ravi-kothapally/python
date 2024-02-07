Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l=['ravi' 'green']
>>> l
['ravigreen']
>>> l[1]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    l[1]
IndexError: list index out of range
>>> d={1:45,2:46}
>>> d
{1: 45, 2: 46}
>>> d[1]
45
>>> d[]
SyntaxError: invalid syntax
>>> d[2]
46
>>> type(d)
<class 'dict'>
>>> d.apend(8:90)
SyntaxError: invalid syntax
>>> d.apend(1:90)
SyntaxError: invalid syntax
>>> (v,b,n)=(1,2,3)
>>> type(b)
<class 'int'>
>>> s={1,2,3,'jk'}
>>> s
{1, 2, 3, 'jk'}
>>> type(s)
<class 'set'>
>>> v={10,20,30,'p','vc'}
>>> v
{'vc', 10, 'p', 20, 30}
>>> v={'ra', 'ra'}
>>> v
{'ra'}
>>> v-s
{'ra'}
>>> s-v
{1, 2, 3, 'jk'}
>>> s+v
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s+v
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> list
<class 'list'>
>>> list(s)
[1, 2, 3, 'jk']
>>> s
{1, 2, 3, 'jk'}
>>> b=list(s)
>>> b
[1, 2, 3, 'jk']
\
>>> b=tuple(s)
>>> b
(1, 2, 3, 'jk')
>>> b=dict(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    b=dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> a=[1,2,5,4]
>>> sorted(a)
[1, 2, 4, 5]
>>> sort(a)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    sort(a)
NameError: name 'sort' is not defined
>>> a.sort();
>>> a
[1, 2, 4, 5]
>>> a
[1, 2, 4, 5]
>>> a=[1,2,5,4]
>>> sorted(a)
[1, 2, 4, 5]
>>> a
[1, 2, 5, 4]
>>> a..sort();
SyntaxError: invalid syntax
>>> a.sort();
>>> a
[1, 2, 4, 5]
>>> 

>>> 
>>> 
>>> 


>>> 

>>> 



>>> vba=(1,2,34)
>>> sorted(vba)
[1, 2, 34]
>>> vba.sort();
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    vba.sort();
AttributeError: 'tuple' object has no attribute 'sort'
>>> a={1,2,3}
>>> sorted(a)
[1, 2, 3]
>>> a.sort();
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.sort();
AttributeError: 'set' object has no attribute 'sort'
>>> #aim
>>> #expected output
>>> #procedure /concepts/algorithm/psuedo
>>> #source code python
>>> #obtained output
>>> #tes cases ---5
