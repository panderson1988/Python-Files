import random

colors = [ 'red', 'yellow', 'green', 'blue' ]
color = random.choice( colors )

# multi-way
def multiway(color):
    '''if color is red print stop, yellow print slow,
    green print go; else print color'''
    
    print('mutli-way if for color = {0}'.format( color ))
    if color == 'red':
        print('red means stop!')

    elif color == 'yellow':
        print('yellow means slow down.')

    elif color == 'green':
        print('green means go.')

    else:
        print('In multi-way else block, color = {0}'.format(color))

    print('In line after multi-way if statement\n')


def ifs(color):
    '''if color is red print stop, yellow print slow,
    green print go; else print color'''
    
    print('mutli-way if for color = {0}'.format( color ))
    if color == 'red':
        print('red means stop!')

    if color == 'yellow':
        print('yellow means slow down.')

    if color == 'green':
        print('green means go.')

    else:
        print('In multi-way else block, color = {0}'.format(color))

    print('In line after multi-way if statement\n')
