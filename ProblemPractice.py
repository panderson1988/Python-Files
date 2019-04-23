#Problem 2

gender = eval (input ('Please enter either m for male, or f for female: '))
age = eval (input ('Please enter your age: '))
if gender == 'f' and age == 10 or gender == 'm' and age in range (9,11):
    print ('Congratulations, you are elgible to join the team')

else:
    print ('Sorry, you are not elgible to join the team')

    
