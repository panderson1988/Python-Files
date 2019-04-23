#Examples from 5.4 onwards

def greetingService():
    'repeatedly requests for users name'
    while True: #While loop is infinite, and it'll continue to ask your name
        name = input('What is your name? ')
        print('Hello {}!'.format(name))

def nominationsWhileLoop():

    successful = [] #Not 0 since we want a list here
    nominees = []

    nomination = input('Please enter a nomination: ').strip()
    while True:
        nomination = nomination.capialize()
        nominees.append(nomination)

        if nomination not in successful and nominees.count(nomination)>1:
            successful.append(nomination)

        nomination = input('Please enter a nomination: ').strip()
        #We need to ask twice in our code to change nomination and to end the infinite loop
    return successful
        

def breakOneLoop(): #To stop a loop
    'prints number sin a list until it encounters first even number'

    lst = [1,3,23,8,5,20,17]
    for i in lst:
        if i%2 == 0: #Reminder, this is to pull even numbers
            break
        print(i, end=' ')


def breakNestedLoop():
    'prints product of lst1 * lst2 until it encounters value of 6'

    for i in range(1,5): #OuterLoop
        for j in range(1,4): #InnerLoop 
            print('i={0}, j={1}'.format(i,j), end=' ')#Show current values

            prod = i*j
            if prod == 6: #Terminate outer loop
                print()
                break

            print('prod: {0}'.format(prod))

        print() #print new line

def continueOneLoop():
    'skip the even numbers, but the loop continues to find odd numbers'

    lst = [1,3,23,8,5,20,17]

    for i in lst:
        if i%2 == 0: #if i is even
            continue #terminate current iteration

        print(i, end =' ')

def continueNestedLoop():
    'prints products of lst 1 * lst 2, except when product = 6'

    for i in range(1,5): #OuterLoop
        for j in range(1,4): #inner loop
            print('i={0}, j{1}'.format(i,j), end=' ') #show current values

            prod = i * j
            if prod == 6: #terminate inner loop
                print()
                continue

            print('prod={0}'.format(prod))

        print () #Print new line

def multiwayIfAction(color):
    'we want the function to retrun a string that corresponds to a color'

    import random
    print (color)

    if color == 'red':
        return 'stop'

    elif color == 'yellow':
        return 'slow down'

    elif color == 'green':
        return 'go'

    elif color == 'flashing red':
        return 'stop sign'

    else:
        return 'color {0} not defined'.format(color)

def getDictAction(color):
    'returns action corresponding to color'

    print(color)

    lights = {'red':'stop',
              'yellow':'slow down',
              'green':'go',
              'flashing red':'stop sign'}

    if color in lights:
        return lights[color]

    else:
        return 'colr {0} not defined'.format(color)

def frequency(my_list): #This example is on d2l
    'function returns a dictionary that maps easch letter in my_lst'

    count = {} #Empty dictionary

    for item in my_list:
        if item in count:
            count[item] += 1 #Increment the item

        else: #adding new key, value pair
            count[item] = 1

    return count

def printCounts(dct)cnt):
    for key,value in dct_cnt.items{}:
        desc = 'time'
        if vlaue > 1:
            desc = 'times'
        print ('{0} appears {1} {2}'.format(key, value, desc))

def wordcount(text):
    'print frequency or each word in text'

    dct = {}

    #text has no punctuation and words separated by blank spaces
    words = text.split()
    for word in words: #iterate over each word
        if word in dct:
            dct[word] += 1 #if word is key in dct, increment count

        #else word is not key in dct
        #add new key, vlaue pair and intitalize value to 1
        else:
            dct [word] = 1

    #print word counts]
    for k,v in dct.items():
        times = ''
        if v == 1
        times = 'time'

    else:
        times = 'times'

    print('{0:10} appears {1} {2}'.format(k,v,times))

def tupleKeys(): #Dictionary with tuple for keys

    dct = { ('c','terry'): 'scrabble'
           ,('j', 'terry'): 'word with friends'
            , ('j', 'henn'): 'life'
            , ('c','mirabelli'): 'monopoly'}

    initial = input('Enter first name initial: ')
    last = input('Enter last name: ')

    if(initial, last) in dct:
        print( '{0} {1}\'s favorite game is {2}'.format(initial, last, dct[(initial, last)]))

    else:
        print('person not found in dictionary')
            



