
# string representations

# if string not enclosed in quotes, interpreted as a variable
>>> They
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    They
NameError: name 'They' is not defined
>>>

# if text contains single quotes, use single quote delimiters and vice versa
>>> "They're here"
"They're here"
>>> 'They are "here"'
'They are "here"'
>>>

# If string contains both types of quotes use \ to escape
# Remember the print() function interprets escape sequence and omits string delimiters
>>> poltergeist = '''They
are here
'''
>>> poltergeist
'They\nare here\n'
>>> print( poltergeist )
They
are here

>>>

# string slice notation
# s[ i:j ] start at index i and end before index j
# s[ :j ] start at index 0 and end before index j
# s[ i: ] start at index i and go to the end
# s[ : ] makes a copy of entire string
# if slice does not exist, result is empty string

>>> s = 'slice'
>>> s[0:3]
'sli'
>>> s[-4:-1]
'lic'
>>> s[:2]
'sl'
>>> s[3:]
'ce'
>>> s[1:4]
'lic'
>>> s[:]
'slice'
>>> s[3:3]
''
>>> s[5:6]
''
>>> 

# slice notation applies to a list as well
>>> lst = [ 2, 4,-1, 5, 8 ]
>>> lst[0:3]
[2, 4, -1]
>>> lst[:2]
[2, 4]
>>> lst[3:]
[5, 8]
>>> lst[2:2]
[]
>>> lst[6:]
[]
>>>

# string methods
# s.capitalize() - returns copy of s with first character capitalized
# s.find( target ) - returns index of first occurrence of target in s, else -1 if not found
# s.lower() - returns lowercase copy of s
# s.upper() - returns uppercase copy of s
# s.replace( old, new ) - returns copy of s with every occurrence of old replaced with new
# s.split( [sep] ) - returns list of substrings of s, delimited by whitespace by default or sep if specified
# s.strip() - returns copy of s without leading and trailing whitespace

>>> s1 = 'eT PHONE HOME'
>>> s1.capitalize()
'Et phone home'
>>> s1.find( 'ph' )
-1
>>> s1.find( 'HOME' )
9
>>> s1.lower()
'et phone home'

>>> s = 'et phone home'
>>> s.find( 'ph' )
3
>>> s.upper()
'ET PHONE HOME'
>>> s.replace( 'phone', 'email' )
'et email home'
>>> s.split()
['et', 'phone', 'home']
>>> s.split(';')
['et phone home']
>>> s = '\tet phone home'
>>> s.strip()
'et phone home'
>>> s='hello\n\there\n'
>>> s.strip()
'hello\n\there'
>>> s1 = 'line1\nline2\nline3'
>>> s1.split()
['line1', 'line2', 'line3']
>>> s1 = 'line1\n line2\n line3'
>>> s1.split()
['line1', 'line2', 'line3']
>>> s1 = 'line1\tline2\tline3'
>>> s1.split()
['line1', 'line2', 'line3']
>>> s1 = 'line1  line2  line3'
>>> s1.split()
['line1', 'line2', 'line3']
>>>
>>> nums = '1,2,3,4,5,6'
>>> lst_str_nums = nums.split(',')
>>> lst_str_nums
['1', '2', '3', '4', '5', '6']
>>>
