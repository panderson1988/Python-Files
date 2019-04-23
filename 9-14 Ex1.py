import math
def hyp(a,b):
    'returns square root of a-squared plus b-squared'
    c = math.sqrt (a**2 + b**2)
    return c

'''>>> hyp(3,4)
5.0
>>> 
'''

def chainedAge():
    name = input('Enter your name')
    age = eval(input('Enter your age'))

    if 13 <= age <= 19:
        print(name, ',congratulations', age, 'you are a teenager')

    else:
        print (name, 'contratulations', age, 'year-old', 'you are not a teen, or an adult')
    
