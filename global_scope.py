def calcProd( n1, n2 ):
    '''
    global variable n3 is accessible inside function
    as long as you do not try to change it
    '''
    prod = n1 * n2 # n1, n2, prod local to calcProd()
    print('n3 inside fn =', n3) # n3 is global n3 if do not try to change
    return prod

n3 = eval(input('enter number for n3: ')) # n3 is global
myProd = calcProd(3,2) * n3 # myProd is global
print('main program n3 =', n3)
print('myProd =', myProd)
