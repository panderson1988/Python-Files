Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 3 + 2
5
>>> 3 -2
1
>>> 3*2
6
>>> 10*2/5
4.0
>>> 3^2
1
>>> 2^5
7
>>> 3//2
1
>>> 14//3
4
>>> 14%3
2
>>> 5**2
25
>>> 2**3-5
3
>>> (1-3+2)**3*4
0
>>> abs(-5*2)
10
>>> min(4,5,20,-30)
-30
>>> max(4,5,40,20,50,-50)
50
>>> x = True
>>> type(x)
<class 'bool'>
>>> y = True
>>> y = true
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    y = true
NameError: name 'true' is not defined
>>> 5 > 4
True
>>> 4 >= 4
True
>>> 4 >= 6
False
>>> 5 == 4
False
>>> 12//5 == (10-2) / 2
False
>>> 5 < 6 or False
True
>>> 9/3 > 2 and 3*2-1 < 4
False
>>> not 4==4.0
False
>>> 5>3 and 2==4 and 2>5
False
>>> False and False
False
>>> True and False
False
>>> True and True
True
>>> (23 + 19 + 31)/3
24.333333333333332
>>> int (23 + 19 + 31)/3
24.333333333333332
>>> abs (54-57)
3
>>> 1387//19
73
>>> 31%
SyntaxError: invalid syntax
>>> (23 + 19 + 31)//3
24
>>> 31 mod 2
SyntaxError: invalid syntax
>>> 31 % 2
1
>>> 1387 mod 19
SyntaxError: invalid syntax
>>> 1387dist19
0
>>> (31%@) == 0
SyntaxError: invalid syntax
>>> (31%2) ==0
False
>>> (1387%19) ==0
True
>>> 1387%19
0
>>> x = 3
>>> x
3
>>> x = 3
>>> y
True
>>> x = 3
>>> x
3
>>> type (x)
<class 'int'>
>>> x = 3 > 4
>>> X
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    X
NameError: name 'X' is not defined
>>> x
False
>>> type (x)
<class 'bool'>
>>> x = 4
>>> x
4
>>> y = x/3
>>> y
1.3333333333333333
>>> number9 = 7
>>> number
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    number
NameError: name 'number' is not defined
>>> number9
7
>>> number = 4
>>> number
4
>>> Number9 = 7
>>> number9
7
>>> Number9 = 9
>>> number9
7
>>> Number9
9
>>> nu mber = 5
SyntaxError: invalid syntax
>>> nu_mber = 5
>>> nu_mber
5
>>> letter_h = "hello"
>>> letter_H = "Hello"
>>> letter_H == letter_h
False
>>> ord ("h")
104
>>> ord ('h')
104
>>> ord ('a')
97
>>> string5 * 2
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    string5 * 2
NameError: name 'string5' is not defined
>>> n = 5
>>> string5 * 2
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    string5 * 2
NameError: name 'string5' is not defined
>>> 'patrick' * 5
'patrickpatrickpatrickpatrickpatrick'
>>> 'patrick' + ' ' + 'is' + ' ' + "here"
'patrick is here'
>>> "patrick" * 2
'patrickpatrick'
>>> "Bono" + ' ' + "hello" * 2
'Bono hellohello'
>>> 'd' in "DePaul"
False
>>> 'D' in 'DePaul'
True
>>> s = 'Apple'
>>> len (s)
5
>>> s = ' A p p l e'
>>> s[0] = A
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    s[0] = A
NameError: name 'A' is not defined
>>> s[0] = 'A'
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    s[0] = 'A'
TypeError: 'str' object does not support item assignment
>>> s[0]
' '
>>> s = 'Apple'
>>> s[0]
'A'
>>> s[5]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    s[5]
IndexError: string index out of range
>>> s[-3]
'p'
>>> Cardinals = ['Leake', 'Holliday', 'Moss', 'Adams'}
SyntaxError: invalid syntax
>>> Cardinals = ['Leake', 'Holliday', 'Moss', 'Adams']
>>> Cardinals
['Leake', 'Holliday', 'Moss', 'Adams']
>>> stuff = [ 'fruit', [0,1], 3>5 ]
>>> stuff
['fruit', [0, 1], False]
>>> type (stuff [0])
<class 'str'>
>>> type (stuff [1])
<class 'list'>
>>> type (stuff [-1])
<class 'bool'>
>>> lst = ['one', 'two', 'four']
>>> lst [2]
'four'
>>> lst [2] = 'three'
>>> lst
['one', 'two', 'three']
>>> s = "a,b,d'
SyntaxError: EOL while scanning string literal
>>> s = 'abd'
>>> s[2]
'd'
>>> s[2] = 'c'
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    s[2] = 'c'
TypeError: 'str' object does not support item assignment
>>> 'leake' in Cardinals
False
>>> 'leake' not in Cardinals
True
>>> 'Leake" in Cardinals
SyntaxError: EOL while scanning string literal
>>> 'Leake' in Cardinals
True
>>> min ( [2,3,4,1] )
1
>>> max ( [2,3,4,1] )
4
>>> len(Cardinals)
4
>>> len(stuff)
3
>>> lst = [2, 4, 6]
>>> lst.append(8)
>>> lst
[2, 4, 6, 8]
>>> lst = ['a', 'b', 'c', 'a']
>>> lst.count('a')
2
>>> lst.count('d')
0
>>> lst = [ 'a', 'b', 'c', 'a' ]
>>> var_pop = lst.pop()
>>> var_pop
'a'
>>> lst = [ 'a', 'b', 'c', 'a' ]
>>> var_remove
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    var_remove
NameError: name 'var_remove' is not defined
>>> var_remove = lst.remove('b')
>>> var_remove
>>> type(var_pop)
<class 'str'>
>>> type(var_remove)
<class 'NoneType'>
>>> lst.pop()
'a'
>>> lst = ['a', 'b', 'd', 'a']
>>> lst_pop(2)
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    lst_pop(2)
NameError: name 'lst_pop' is not defined
>>> lst.pop(2)
'd'
>>> lst.pop() * 4
'aaaa'
>>> s1 = 'ant'
>>> s2 = 'bat'
>>> s3 = 'cod'
>>> str = 's1' + ' ' + 's2' + ' ' + 's3'
>>> 's1' + ' ' + 's2' + ' ' + 's3'
's1 s2 s3'
>>> s1 + ' ' + s2 + ' ' + s3
'ant bat cod'
>>> s1 + ' ' + s2 + ' ' + s2 + ' '+ s3
'ant bat bat cod'
>>> s2*2 + s3 + ' ' + s2*2 + s3 + ' '
'batbatcod batbatcod '
>>> s1 + ' ' + (2*(s2+' ')) + s3
'ant bat bat cod'
>>> 2* (2*s2 + s3 + ' ')
'batbatcod batbatcod '
>>> x = 2
>>> type (x)
<class 'int'>
>>> type (1.3)
<class 'float'>
>>> type ('')
<class 'str'>
>>> type ([])
<class 'list'>
>>> 
