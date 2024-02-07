Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("hi ravi')
      
SyntaxError: EOL while scanning string literal
>>> SyntaxError: EOL while scanning string literal
SyntaxError: invalid syntax
>>> name="ravi"
>>> name
'ravi'
>>> #one liner swap
>>> a=6
>>> b=9
>>> a,b=b,a
>>> a,b
(9, 6)
>>> #10-07-2018
>>> #dynamic typed languAGE
>>> x=1
>>> x=x/2
>>> x
0.5
>>> print(type(x))
<class 'float'>
>>> x=1
>>> print(type(x))
<class 'int'>
>>> #reassignment
>>> 5+2
7
>>> #as calcy
>>> 5-2
3
>>> 5*2
10
>>> 5**2
25
>>> 5%2
1
>>> 5//2
2
>>> #literals
>>> print('hello')
hello
>>> print("hello")
hello
>>> print("'hello"')
      
SyntaxError: EOL while scanning string literal
>>> print('''hello'''0
      
SyntaxError: invalid syntax
>>> print('''hello''')
hello
>>> a='hello'
>>> a
'hello'
>>> b='hello'
>>> a==b
True
>>> a1=b
>>> a1
'hello'
>>> a1!=b
False
>>> a1*b
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a1*b
TypeError: can't multiply sequence by non-int of type 'str'
>>> a1+b
'hellohello'
>>> a1+' ' +b
'hello hello'
>>> 
>>> 
>>> D='hi'
>>> D
'hi'
>>> d
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> d='hi"
SyntaxError: EOL while scanning string literal
>>> #escape sequences.../n  /t \' \" \\
>>> print("ravi \n")
ravi 

>>> print("ravi \t sun")
ravi 	 sun
>>> print("ravi \n sun")
ravi 
 sun
>>> print("ravi \' sun")
ravi ' sun
>>> print("ravi \\ sun")
ravi \ sun
>>> print("ravi \" sun")
ravi " sun
>>> print(ravi)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(ravi)
NameError: name 'ravi' is not defined
>>> # \r \a
>>> print("ravi \r sun")
ravi  sun
>>> print("ravi \a sun")
ravi  sun
>>> print("ravi \b sun")
ravi  sun
>>> print("ravi\"")
ravi"
>>> print(""ravi"")
SyntaxError: invalid syntax
>>> #raw strings
>>> print(r"what \'s hii")
what \'s hii
>>> print("what \'s hii")
what 's hii
>>> print(R"what \'s hii")
what \'s hii
>>> #variables and identifiers
>>> 1r=3
SyntaxError: invalid syntax
>>> r1=3
>>> r1
3
>>> r@=2
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    r@=2
NameError: name 'r' is not defined
>>> r#
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    r#
NameError: name 'r' is not defined
>>> r#=3
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    r#=3
NameError: name 'r' is not defined
>>> r%=3
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    r%=3
NameError: name 'r' is not defined
>>> r$
SyntaxError: invalid syntax
>>> r$=4
SyntaxError: invalid syntax
>>> my-var=3
SyntaxError: can't assign to operator
>>> #variable assignment
>>> a,b,c=5,3.2,"hello"
>>> a,b,c
(5, 3.2, 'hello')
>>> #keywords cannot be used as identifiers
>>> global=7
SyntaxError: invalid syntax
>>> #multi-line statements
>>> a=1+2+3+4+\#continuation character
SyntaxError: unexpected character after line continuation character
>>> a=1+2+3+4+\ 4
SyntaxError: unexpected character after line continuation character
>>> a=1+2+3+4+\
   4+5+6
>>> a
25
>>> #SINGLE LINE
>>> msg="pora";print(msg)
pora
>>> 			#assignments
>>> i=5
>>> a="ravi",b=9.24,c="b151348"
SyntaxError: can't assign to literal
>>> print(a,b,c)
25 3.2 hello
>>> a="ravi",b=9.24,c="b151348"
SyntaxError: can't assign to literal
>>> a="ravi"
>>> b=9.24
>>> print(a.b)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    print(a.b)
AttributeError: 'str' object has no attribute 'b'
>>> print(a,b)
ravi 9.24
>>> a,b,c="ravi",8,8.9
>>> a,b,c
('ravi', 8, 8.9)
>>> a=b=c="pora sunny ga"
>>> a
'pora sunny ga'
>>> 		#reassignment
>>> x=10
>>> x=x/11
>>> x
0.9090909090909091
>>> x=22/7
>>> x
3.142857142857143
>>> 
