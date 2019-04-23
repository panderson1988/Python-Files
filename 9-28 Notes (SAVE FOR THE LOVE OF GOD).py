#Example 1 for counter loop pattern

def counterLoopDivFour(n):
    for i in range (4, n+1): #Page 4
        if i % 4 == 0:
            print (i)

def counterLoopList():
    lst = ['hello', 'arthur', 'foo', 'bar']
    for i in range(len(lst)): #1 for i in range (4)
        print('item at index {0} = {1}'.format(i, lst[i]))
        #Page 5
        #Was this tied to homework 3???

#Practice Example in class, based on pages 4 or 5
#Practice Example 'multiples'

def multiples (lst,num):
    for i in range(len(lst)):
        if lst[i] != num * (i +1):
            return False

    return True

#I'm keeping the last example without editing it

def multiples2 (lst,num):
    for i in range (len (lst)):
        print ('i={0}'.format(i))
        print ('i+1 = {0}'.format(i+1))
        print ('res = {0}'.format(num * (i+1)))
        print()
        if lst[i] != num * (i+1):
            return False

    return True

#example is on page 7

def checkSorted(lst):
    for i in range (len(lst)-1):
        if lst [i] > lst [i +1]:
            return False
    return True

#Example on accumulator variable on page 7-8
               
def manualSum(lstNums):
    '''return sum of lstNums'''
    mySum = 0 #accumulator variable
    for num in lstNums:
        mySum += num #shorthand for mySum = mySum + num
    return mySum

#Example indexes on page 8

def indexes (word, char):
    indies = [] #accumulator variable

    for index in range(len(word)):
        if word[index] == char:
            indies.append((index))
    return indies


#Excercise

def factorial (num):
    '''
    return num!
    '''

    fac = 1 #accumulator variable
    for i in range (2, num + 1):
        fac = fac * i #shorthand is fac *= i

    return fac

def timesTables():

    for outer in range(2,5):
        print('times table for {0}'.format(outer))

        for inner in range(1,6):
            print ('{0} x {1} = {2}'.format(outer, inner, outer*inner))

        print () #print blank line

#look at pairSum() exercise on page 9 and 10
