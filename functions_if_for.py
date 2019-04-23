
##### running a module/file #####
'''
F5 - runs module (needs to be saved CTRL-s)
this restarts the shell and
executes all code in the module/file
results of expressions are NOT
automatically displayed

you can print things you want to display
'''

##### def #####

'''
function definition, does
not actually run the code
it just names it

all statments inside must be indented
first non-indented statements marks
the end of the fucnction
'''

##### functions - no parameters #####

def f1():
    x = 7*12

    # function does not return a value, just displays (prints)
    print(4+5)
    print(x)

'''
>>> ================================ RESTART ================================
>>> 
>>> f1()
9
84
'''

# one-way
def votingage():
    age = eval( input( 'Enter your age: ') ) # a number

    if age >= 18:
        print( 'You can vote!' )


# two-way
def votingage():
    age = eval( input( 'Enter your age: ' ) ) # a number

    if age >= 18:
        print( 'You can vote!' )

    else: 
        print( 'You cant vote' )
        print( 'Wait',18-age,'years.' )

    print( 'Thanks, bye bye' )

'''
>>> votingage()
Enter your age: 37
You can vote!
Thanks, bye bye
>>> votingage()
Enter your age: 12
You cant vote
Wait 6 years.
Thanks, bye bye
'''

##### functions - parameter passing #####

# first version prints
def max_num_print( a, b ): # like saying a=2,b=3

    if a > b:
        print( a )

    else:
        print( b )

''' Pass in values to function without prompting
>>> max_num_print( 2, 3 )
3
'''

# return version
# allows assignment of result
def max_num_return( a, b ): # like saying a=first,b=second and first==2, second==3
    if a > b:
        return a

    else:
        return b

'''Prompt for values to pass into function
assign result of function call to a variable the_max
>>> first = eval( input( 'enter first number: ' ) )
enter first number: 2
>>> second = eval( input( 'enter second number: ' ) )
enter second number: 3
>>> the_max = max_num_return( first, second )
>>> the_max
3
'''

# nested control flow structures:
# combine iteration structure with conditional structure
def vowelstart( word_lst ): # word_lst = lst and lst==[ 'hello','apple','pear','orange' ]
    for word in word_lst:
        # if word starts with vowel
        if word[0] in 'aeiouAEIOU':
            print( word )
    
'''
>>> lst = [ 'hello','apple','pear','orange' ]
>>> vowelstart( lst )
apple
orange
'''





    
