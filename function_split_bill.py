'''
Three people ate dinner at a restaurant and want to split the bill. 
The total is $35.27, and they want to leave a 15% tip.  
How much should each person pay?
'''

total = 35.27
totalPlusTip = 35.27 * 1.15
amtPerPerson = totalPlusTip / 3

print( 'amount per person =', amtPerPerson )


# use a function to compute the amount each person pays
def split_bill( bill, tip, num_ppl ):
    '''
    Add tip to bill to calculate total bill including tip.
    Split total between num_ppl and return that value
    rounded to two digits
    '''

    tip_pct = tip / 100
    
    # total_bill can also be written as bill + ( bill * tip percentage )
    total_bill = bill * ( 1 + tip_pct )
    amt = total_bill / num_ppl

    return round( amt, 2 )

''' Algorithm
-split_bill() function requires three parameters that are specified in the def
-prompt user for bill_amt and assign value to variable bill_amt
-prompt user for tip_amt and assign that value to tip_amt
-prompt user for number of people and assign that value to folks
-call split_bill passing in three values bill_amt, tip_amt, folks
 and assign return value to variable amt_per_person
-print amt_per_person
'''


'''
>>> ================================ RESTART ================================
>>> 
>>> bill_amt = eval( input( 'enter bill amount: ' ) )
enter bill amount: 35.27
>>> tip_amt = eval( input( 'enter tip amount between 10 and 20: ' ) )
enter tip amount between 10 and 20
>>> folks = eval( input( 'enter number of people: ' ) )
enter number of people: 3
>>> amt_per_person = split_bill( bill_amt, tip_amt, folks )
>>> print( 'Amount per person = $', amt_per_person )
Amount per person = $ 13.52
'''
