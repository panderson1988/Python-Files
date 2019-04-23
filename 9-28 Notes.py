Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Syntax Error, anything with an incorrect format
>>> Example = (3+4]
SyntaxError: invalid syntax
>>> #Tuples are comma, ',' delimited
>>> #Erroneous state errors occur when syntax was correct, but input wasn't
>>> 4*2
8
>>> '4' * '2'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    '4' * '2'
TypeError: can't multiply sequence by non-int of type 'str'
>>> #Traceback goes back to the line of the error

>>> #We won't get through 5.5, 5.6 tonight
>>> #Reminder: one-way if - if <condition>, then code executes
>>> #Two way if/else
>>> #Multiway if starts with if, then "elif." You can have multiple ifs
>>> #You aren't required to have else, but if none conditions occur, then nothing will happen
>>> #No else will go to a non-indented statement
>>> '''
>>> help (multiway)
Help on function multiway in module __main__:

multiway(color)
    if color is red print stop, yellow print slow,
    green print go; else print color

>>> multiway('green')
mutli-way if for color = green
green means go.
In line after multi-way if statement

>>> multiway('red')
mutli-way if for color = red
red means stop!
In line after multi-way if statement
'''
"\n>>> help (multiway)\nHelp on function multiway in module __main__:\n\nmultiway(color)\n    if color is red print stop, yellow print slow,\n    green print go; else print color\n\n>>> multiway('green')\nmutli-way if for color = green\ngreen means go.\nIn line after multi-way if statement\n\n>>> multiway('red')\nmutli-way if for color = red\nred means stop!\nIn line after multi-way if statement\n"
>>> open ('multiway_vs_ifs.py')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    open ('multiway_vs_ifs.py')
FileNotFoundError: [Errno 2] No such file or directory: 'multiway_vs_ifs.py'
>>> import os
>>> open ('multiway_vs_ifs.py')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    open ('multiway_vs_ifs.py')
FileNotFoundError: [Errno 2] No such file or directory: 'multiway_vs_ifs.py'
>>> #If you use only if statements over elif statements, then it'll execute other lines of   code unlike elif
>>> #In example provided, it printed both if and else since the code didn't stop running      after meeting one true if statement
>>> #Full notes in textpad ++
>>> def iteratoinLoopString():
	for char in 'cookies':
		print (char)

		
>>> iterationLoopString()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    iterationLoopString()
NameError: name 'iterationLoopString' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> iterationLoopFileChar('sample.txt')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    iterationLoopFileChar('sample.txt')
NameError: name 'iterationLoopFileChar' is not defined
>>> #Idiot, you don't have that file in your python foler
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> counterLoopDivFour(10)
4
8
>>> counterLoopDivFour(16)
4
8
12
16
>>> 
=============================== RESTART: Shell ===============================
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> counterLoopList()
item at index 0 = hello
item at index 1 = arthur
item at index 2 = foo
item at index 3 = bar
>>> 
=============================== RESTART: Shell ===============================
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> multiples ([3,6,9],3)
True
>>> mutiples ([2,3,6,9],2)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    mutiples ([2,3,6,9],2)
NameError: name 'mutiples' is not defined
>>> multiples([2,3,4,5],2)
False
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> 
=============================== RESTART: Shell ===============================
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> multiples2([3,6,8],3)
i=0
i+1 = 1
res = 3

i=1
i+1 = 2
res = 6

i=2
i+1 = 3
res = 9

False
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> checkSorted(['cat', 'dog', 'mouse'])
True
>>> checkSorted(['red', 'purple', 'grey'])
False
>>> 
=============================== RESTART: Shell ===============================
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> manualSum([3,4,5,6])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    manualSum([3,4,5,6])
  File "C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py", line 52, in manualSum
    mySum += num #shorthand for mySum = mySum + num
UnboundLocalError: local variable 'mySum' referenced before assignment
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> manualSum([3,4,5,6])
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    manualSum([3,4,5,6])
  File "C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py", line 52, in manualSum
    mySum += num #shorthand for mySum = mySum + num
UnboundLocalError: local variable 'mySum' referenced before assignment
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> manualSum([3,4,5,6])
