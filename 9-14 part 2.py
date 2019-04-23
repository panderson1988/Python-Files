Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======= RESTART: C:/Users/panderson1988/Desktop/Python/firstProgram.py =======
This is my first program
This is the second line of my first program
>>> firstLine
'This is my first program'
>>> print ('firstLine')
firstLine
>>> print (firstLine)
This is my first program
>>> 
=============================== RESTART: Shell ===============================
>>> 
======= RESTART: C:/Users/panderson1988/Desktop/Python/firstProgram.py =======
This is my first program
This is the second line of my first program
Adding a third line to my first program
>>> 
=============================== RESTART: Shell ===============================
>>> print (5)
5
>>> print ( 6 == 4)
False
>>> age = input ('enter your age')
enter your age 20
>>> age
' 20'
>>> type (age)
<class 'str'>
>>> age = input ('enter your age')
enter your age: 20
>>> age
': 20'
>>> age = input ('enter your age: ')
enter your age: 20
>>> age
'20'
>>> type (age)
<class 'str'>
>>> eval ( '3>4')
False
>>> eval ( 'max(-1, 4, -5, 8, 2)')
8
>>> age = eval (input ( 'enter your age: '))
enter your age: 20
>>> age
20
>>> 3 > 4 > 6
False
>>> 3 > 2 < 6
True
>>> int( eval('3<4'))
1
>>> int(True)
1
>>> int(False)
0
>>> 
========= RESTART: C:/Users/panderson1988/Desktop/Python/onewayIf.py =========
enter temperature: 86
Goodbye
>>> 
========= RESTART: C:/Users/panderson1988/Desktop/Python/onewayIf.py =========
enter temperature: 95
It is too hot
Be sure to wear sunscreen
Goodbye
>>> 
========= RESTART: C:/Users/panderson1988/Desktop/Python/twowayIf.py =========
enter temperature: 86
It is warm
Be on the lookout for rising temps
Goodbye
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/forString.py ========
char is S
char is t
char is a
char is n
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/forString.py ========
char is S
char is s
char is s
char is s
char is s
char is s
char is s
char is s
char is s
char is t
char is t
char is t
char is t
char is t
char is t
char is t
char is t
char is t
char is a
char is a
char is a
char is a
char is a
char is a
char is a
char is a
char is a
char is a
char is n
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/forString.py ========
char is S
char is t
char is a
char is n
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/forString.py ========
char is S
- Randy Marsh
char is t
- Randy Marsh
char is a
- Randy Marsh
char is n
- Randy Marsh
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/forString.py ========
char is S
char is t
char is a
char is n
- Randy Marsh
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/forString.py ========
char is S
char is t
char is a
char is n
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/forString.py ========
char is S
char is t
char is a
char is n
pet is cat
pet is dog
pet is gerbil
pet is parrot
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/forString.py ========
char is S
char is t
char is a
char is n

Traceback (most recent call last):
  File "C:/Users/panderson1988/Desktop/Python/forString.py", line 7, in <module>
    print ('pet is', pet)
NameError: name 'pet' is not defined
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/forString.py ========
char is S
char is t
char is a
char is n

pet is cat
pet is dog
pet is gerbil
pet is parrot
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/printEven.py ========
enter a list of 5 numbers: '1, 2, 3, 4, 5'
Traceback (most recent call last):
  File "C:/Users/panderson1988/Desktop/Python/printEven.py", line 3, in <module>
    if num % 2 == 0:
TypeError: not all arguments converted during string formatting
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/printEven.py ========
enter a list of 5 numbers: 1, 2, 3, 4, 5
1 is odd
Done
2
Done
3 is odd
Done
4
Done
5 is odd
Done
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/printEven.py ========
enter a list of 5 numbers: 2, 3, 4, 5, 6
2
Done
3 is odd
Done
4
Done
5 is odd
Done
6
Done
>>> 
=============================== RESTART: Shell ===============================
>>> for i in range (4):
	print (i)

0
1
2
3
>>> for i in range (1,5)
SyntaxError: invalid syntax
>>> for i in range (1,5):
	print (i)

	
1
2
3
4
>>> for i in range (5,15):
	print (i)

	
5
6
7
8
9
10
11
12
13
14
]
>>> print (i)
14
>>> 
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/FunctionEx.py ========
>>> restult_f = f(x)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    restult_f = f(x)
NameError: name 'x' is not defined
>>> result_f = f(2)
>>> type(result_f)
<class 'NoneType'>
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/FunctionEx.py ========
>>> result_f = f(2)
14
>>> 
======== RESTART: C:/Users/panderson1988/Desktop/Python/FunctionEx.py ========
>>> result_f = f(2)
>>> result
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    result
NameError: name 'result' is not defined
>>> result_f
14
>>> f(2) * 2
28
>>> 
====== RESTART: C:/Users/panderson1988/Desktop/Python/DocAndComments.py ======
>>> result = f(2)
>>> f
<function f at 0x03EA7738>
>>> help (g)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    help (g)
NameError: name 'g' is not defined
>>> 
====== RESTART: C:/Users/panderson1988/Desktop/Python/DocAndComments.py ======
>>> help(g)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    help(g)
NameError: name 'g' is not defined
>>> 
====== RESTART: C:/Users/panderson1988/Desktop/Python/DocAndComments.py ======
>>> help(g)
Help on function g in module __main__:

g(x, y)
    returns x times 2, plus 10

>>> 
====== RESTART: C:/Users/panderson1988/Desktop/Python/DocAndComments.py ======
>>> f(2)
14
>>> return res
SyntaxError: 'return' outside function
>>> 
