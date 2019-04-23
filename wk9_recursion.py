
#first attempt, recursive step
def countdown1( n ):

    print( n )
    countdown1( n-1 )


#with base case
def countdown2( n ):

    print( n )

    if n == 1:
        print( 'Lift off' )
        return

    else:
        countdown2( n-1 )

#same output, but using different base case
def countdown(n):

    if n == 0:
        print( 'Lift off' )
        return
    
    else:
        print( n )
        countdown( n-1 )

#what does this function do? Trace small examples
def mystery1( n ):

    if n == 0:
        print( 'Lift off' )
        return
    
    else:
        print( n )
        mystery1( n-1 )
        print( n )

#what does this function do? Trace small examples
def mystery( n ):

    if n == 0:
        print( 'Lift off' )
        return

    else:
        print( n )
        print( n )
        mystery( n-1 )

#print letters vertically, first step, splitting string
def vert1( s ):

    print( s[0] )
    print( s[1:] )

#without base case (error message), and second print for tracing
def vert2( s ):

    print( s[0] )
    print( 's[1:]', s[1:] ) #for tracing, comment out for output
    vert2( s[1:] )

#with base case
def vert3(s):

    if s == '':
        return
    
    print( s[0] )
    vert3( s[1:] )

#same output, but different recursive step (separating last letter)
#line numbers for tracing frames on stack
def vert(s):

    if s == '':     #1
        return      #2
                    #3
    vert(s[:-1])    #4
    print(s[-1])    #5


# non-recursive
def dsIter( i ):

    str_i = str( i )
    total = 0
    
    for n in str_i:
        total += int( n )

    return total

#digitsum example, as one-liner
def ds( i ):

    if i == 0:
        return 0
    
    return ds( i//10 ) + ( i % 10 )

#same, different base case
def ds1( i ):

    if i < 10:
        return i
    
    return ds1( i//10 ) + ( i % 10 )

#in more detail,  but same functionality
def ds2(i):

    if i < 10:
        return i

    last_digit = i % 10
    rem_digit = i //10
    rem_digit_sum = ds2(rem_digit)
    
    return rem_digit_sum + last_digit

# return n-th Zimin word
# string over an alphabet with identical prefix and suffix
def Zimin(n):
    'return n-th Zimin word'
    if n == 0:
        return '0'
    
    else:
        Z = Zimin(n-1)
        return Z + str(n) + Z


#same as above, but using that repeatedly subtracting b from a
#until result is less than b is the same as going to a%b directly
def gcd1(a,b):
    'calculate greatest common divisor of a and b'    

    print(a,b) #uncomment for tracing values
    if a < b:
        a,b = b,a

    if b == 0:
        return a

    else:
        return gcd1(b, a%b)


