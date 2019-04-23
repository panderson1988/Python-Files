def divideMe2 (a,b):
    '''
    return decimal division of a divided by b.
    if b == 0, return -1
    '''

    try:
        return a/b
    except:
        print('division by zero not allowed')
        return -1
