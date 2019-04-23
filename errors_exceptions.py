
# Parser component of Python interpreter detects syntax errors
# Syntax error occur due to incorrect format
# Syntax errors occur BEFORE Python executes the statement

>>> (3 + 4]
SyntaxError: invalid syntax
>>>
>>> if x <= 7
SyntaxError: invalid syntax
>>>
>>> tup = ('a'; 'b'; 'c')
SyntaxError: invalid syntax
>>> 
>>> for item in range(4):
print(item)
SyntaxError: expected an indented block
>>> 
>>> 4th_letter = 'd'
SyntaxError: invalid syntax
>>>

# Other type of errors occur during execution of program
# This type of error, commonly called runtime error, raises an exception
# Exception has a type; common types are NameError, TypeError, ZeroDivisionError
# Exception also contains information about the error
# With runtime error, syntax is correct
# Default behavior when exception raised is to halt execution and print error information
>>> 4/0
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    4/0
ZeroDivisionError: division by zero
>>> 
>>> '4' * '2'
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    '4' * '2'
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
>>> a
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
>>> lst = [ 0,1,2,3,4 ]
>>> lst[5]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    lst[5]
IndexError: list index out of range
>>> 
