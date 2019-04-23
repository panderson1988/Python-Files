Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:/Users/panderson1988/Desktop/Python/9-14 Ex1.py =========
>>> help(hyp)
Help on function hyp in module __main__:

hyp(a, b)

>>> hyp(3,4)
5.0
>>> 
========= RESTART: C:/Users/panderson1988/Desktop/Python/9-14 Ex1.py =========
>>> name = 'Patrick"
SyntaxError: EOL while scanning string literal
>>> name = Patrick
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    name = Patrick
NameError: name 'Patrick' is not defined
>>> chainedAge
<function chainedAge at 0x03543108>
>>> name
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> name = 'Patrick'
>>> age = '27'
>>> print
<built-in function print>
>>> print chainedAge
SyntaxError: Missing parentheses in call to 'print'
>>> print (chainedAge)
<function chainedAge at 0x03543108>
>>> 
========= RESTART: C:/Users/panderson1988/Desktop/Python/9-14 Ex3.py =========
>>> bill_amt - eval (input ('enter bill amount: '))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    bill_amt - eval (input ('enter bill amount: '))
NameError: name 'bill_amt' is not defined
>>> bill_amt = eval (input ('enter bill amount: '))
enter bill amount: 35.27
>>> tip_amt = eval (input('enter tip amount between 10 and 20: '))
enter tip amount between 10 and 20: 15
>>> folks = eval (input ('enter number of people: '))
enter number of people: 3
>>> amount_per_person = split_bill(bill_amt, tip_amt, folks
