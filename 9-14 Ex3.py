import math
def split_bill (bill, tip, num_ppl):
    '''
    Add tip to bill to caculate totla bill including tip,
    Split total between num_ppl and return that value
    ronded to two digits
    '''

    tip_pct = tip/100

    # total_bill can also be written as bill + (bill * tip percentage)
    total_bill = bill * (1 + tip_pct)
    amt - total_bill / num_ppl

    return round (amt, 2)

