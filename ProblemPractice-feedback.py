#Problem 2

#CEM here you have parameters when problem says no parameters
#remember parameters are part of function definition
def isElgible(gender,age):
    #CEM gender is a string value so do not need to use eval()
    gender = eval (input ('Please enter either m for male, or f for female: '))
    age = eval (input ('Please enter your age: '))

    #CEM when checking age range, make sure to use chained comparison as
    #stated in directions
    if gender == 'f' and age == 10 or gender == 'm' and age in range (9,11):
        print ('Congratulations, you are elgible to join the team')

    else:
        print ('Sorry, you are not elgible to join the team')

#CEM when you call from interactive shell, since it does not
#have parameters, you just to >>> isEligible()


'''
Sorry, this will be my last email today, but I went ahead
and practiced problem 2 in a separate document to get a feel
for it. The good news is I did get the two way if/else
statement to run properly. That said, when I attempt to
define "isElgible()", then when I run the program it won't
allow me to input gender or age. When I don't define isElgible,
then when I run the program it asks to input the person's
gender, then age, then evaluates the input. 

I believe my problem is I am screwing up how to define functions,
then how to pull up those functions when I run the modules.
I'm including my current definition of a function, but I know
I'm missing something basic here.
'''
