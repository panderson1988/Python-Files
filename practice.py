
def g( y ):
    global x #Global x variable here since we are calling the global variable
    #x = 10 #Local x variable since this x is being defined within the function
    print( 'g() local vars:', vars() ) #Prints local variable g(y)
    print()#local print statement
    return x*y #returns the local calculation of x * y, FYI x here is local since we defined it within this function after the global x


x = 5
