'''
Write a function space( word ) that one parameter, word, consisting of a single word.
The function spaces out the word by inserting spaces between the letters.
Do not use any loops or replace() tricks; solution must use recursion.
If you have an extra space at the end of the word, reconsider/play with your base case.
'''

def space( word ):
    'docstring'

    if len(word) <= 1:
        return word

    else:
        return space( word[:-1] ) + ' ' + word[-1]


def silly(n):
    '''
    docstring
    '''
    if n<0:
        print ('n must be a non-negative integer')
        return

    if n == 0:
        return

    else:
        print ('*', end='')
        silly(n-1)
        print('!', end='')

silly(0)
silly(1)
silly(2)
silly(3)
        
