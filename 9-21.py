Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 3
>>> b = 3.3.
SyntaxError: invalid syntax
>>> a = 3
>>> b = 3.3
>>> c = 'three'
>>> d = [1,7,3}
SyntaxError: invalid syntax
>>> d = [1, 7, 3]
>>> a
3
>>> a = 3
>>> b = 5
>>> a, b = b, a
>>> a
5
>>> b
3
>>> 'They are here'
'They are here'
>>> "They are here"
'They are here'
>>> 'They\'re here'
"They're here"
>>> 'They\'re "here"'
'They\'re "here"'
>>> ''' they
are here
'''
' they\nare here\n'
>>> poltergeist = ''' they
are here'''
>>> poltergeist
' they\nare here'
>>> print (poltergeist)
 they
are here
>>> '''they
are here'''
'they\nare here'
>>> s = 'foobar'
>>> s[-3]
'b'
>>> s[2]
'o'
>>> s = slice
>>> s[0:3]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s[0:3]
TypeError: 'type' object is not subscriptable
>>> s = 'slice'
>>> s[0:3]
'sli'
>>> s = Pennsylvania
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s = Pennsylvania
NameError: name 'Pennsylvania' is not defined
>>> s = 'Pennsylvania'
>>> s[:3]
'Pen'
>>> s[3:]
'nsylvania'
>>> s[-1:]
'a'
>>> s[:-1]
'Pennsylvani'
>>> s{5:}
SyntaxError: invalid syntax
>>> s[5:]
'ylvania'
>>> s[10:]
'ia'
>>> s[15:]
''
>>> s = 'hello'
>>> s.find('d')
-1
>>> s.find('h')
0
>>> s.find('z')
-1
>>> s1 = 'eT PHONE HOME'
>>> s1.capitalize()
'Et phone home'
>>> s1.lower()
'et phone home'
>>> s1.capitalize()
'Et phone home'
>>> s1
'eT PHONE HOME'
>>> s = 'st phone home'
>>> s.find('ph')
3
>>> s.find('home')
9
>>> s.find('Home')
-1
>>> s.split()
['st', 'phone', 'home']
>>> s.split (':')
['st phone home']
>>> s.split(3)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s.split(3)
TypeError: Can't convert 'int' object to str implicitly
>>> s = '   et phone home'
>>> s.strip()
'et phone home'
>>> s = 'hello
SyntaxError: EOL while scanning string literal
>>> s = 'hello\nthere\n'
>>> s
'hello\nthere\n'
>>> print (s)
hello
there

>>> s = 'etphonehome'
>>> s.split(t)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s.split(t)
NameError: name 't' is not defined
>>> var = 'num_one'
>>> print (var,'a',[2,3,4])
num_one a [2, 3, 4]
>>> pets = ['boa', 'cat', 'dog']
>>> for pet in pets:
	print (pet)

	
boa
cat
dog
>>> for pet in pets:
	print (pet, end='!!!')

	
boa!!!cat!!!dog!!!
>>> for pet in pets:
	print (pet, end=',')

	
boa,cat,dog,
>>> for i in range(1,4)
SyntaxError: invalid syntax
>>> for i in range (1,4):
	print(i, i**2, sep='::', end='!!')

	
1::1!!2::4!!3::9!!
>>> weekday = 'Wednesday'
>>> month = 'March'
>>> day = 10
>>> year = 2010
>>> hour = 11
>>> minute = 45
>>> second = 33
>>> print ('{}:{}:{}'.format(hour, minute, second))
11:45:33
>>> print ('{}, {} {}, {} {}:{}:{}'.format(weekday, month, day, year, hour, minute, second))
Wednesday, March 10, 2010 11:45:33
>>> for i in range (1,8):
	print (i, i**2, i**3)

	
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
>>> #Note, it basically shows the range 1-7, then applies math for each call to action
>>> for i in range(1,8)
SyntaxError: invalid syntax
>>> for i in range(1,8):
	print('{0:2} | {1:2} | {2:4}'.format(i, i**2, i**3))

	
 1 |  1 |    1
 2 |  4 |    8
 3 |  9 |   27
 4 | 16 |   64
 5 | 25 |  125
 6 | 36 |  216
 7 | 49 |  343
>>> #Reference notes on page 6 to understand why it is 2:4

>>> #Reference notes on page 6 to understand spaces and with ex 2:4
>>> lst = ['Alan Turing', 'Ken Thompson', "Vint Cerf']
       
SyntaxError: EOL while scanning string literal
>>> lst = ['Alan Turning', 'Ken Thompson', 'Vint Cerf']
>>> for name in lst:
	f1 = name.split()
	print(f1[0], f1[1])

	
Alan Turning
Ken Thompson
Vint Cerf
>>> for name in lst:
	f1 = name.split()
	print('{0:5}{1:10}!'.format(f1[0], f1[1]))

	
Alan Turning   !
Ken  Thompson  !
Vint Cerf      !
>>> #Note, this is on page 7
>>> '{0:.2f}'.format(6.388)
'6.39'
>>> os.getcwd()
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    os.getcwd()
NameError: name 'os' is not defined
>>> 
