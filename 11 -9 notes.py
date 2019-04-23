#Problem 11
def trace2():
    lst = [1, -5, 4, 2]
    total = sum(lst)
    index = 0
    while index < len(lst):
        index += 1
        print('index=', index)
        total += index
        print('total =', total)
        if total >=4:
            continue
        index += 1

    print (total)

#Problem 12
def trace11():
    '''returns index of smallest value in lst'''
    lst = list(range(4, -7, -3))
    lst.append(20)
    lst.append(-12)
    lst.append(5)
    lst.append(-7)
    print(lst)
    indexOfLeast = 0
    for i in range(1, len(lst)):
        if lst [i] , lst[indexOfLeast]:
            indexOfleast = i
    print (indexOfLeast)
    
