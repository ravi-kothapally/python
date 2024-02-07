Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 					#identation
>>> for i in range(1,11)
SyntaxError: invalid syntax
>>> for i in range(1,11):
	print(i)

	
1
2
3
4
5
6
7
8
9
10
>>> for i in(1,11):
	print(i)

	
1
11
>>> for i in(1,11):
	print(i**2)

	
1
121
>>> for i in(1,11):
	print(i)
	if i==5:
		break;

	
1
11
>>> for i in(1,11):
	print(i)
	if i==1:
		break;

	
1
>>> for i in(1,5,6,7,11):
	print(i)
	if i==1:
		break;

	
1
>>> for i in(1,5,6,7,11):

print(i)
	if i==1:
		break;
	
SyntaxError: expected an indented block
>>> for i in range(0,3)
SyntaxError: invalid syntax
>>> for i in range(0,3):
	{
		print(i)
	}

	
0
{None}
1
{None}
2
{None}
>>> 5>>5
0
>>> 5<<5
160
>>> 5%6
5
>>> 5&5
5
>>> 5&6
4
>>> 5|6
7
>>> !5
SyntaxError: invalid syntax
>>> not 5
False
>>> ! 5
SyntaxError: invalid syntax
>>> x=!5
SyntaxError: invalid syntax
>>> ~5
-6
>>> 5 in (1,2,3,4,5)
True
>>> 5  not in (1,2,3,4,5)
False
>>> 
