
#Notes 10/19

#Example with Scope and Global Namespace, page 3

#scope vars

def calcProd2(n1, n2):
    prod = n1 * n2
    global n3
    n3 - 5
    print('n3 inside fn =', n3)
    print()
    print('local calculateProd() namespace variables\n', vars())

n3 = 6
print('n3 before fn call=', n3)
myProd = calcProd2(3,2) * n3
print('myProd =', myProd)
print()
print('global namespace variables\n', vars()

#Look at stack01.py

#Notes

defar(a):
    b=a*2
    a=a+3
    print("a=", a, "b=", b)

def foo(x,y)
    x = x+1
    z = x+y
    bar(z)
    print("x=", x, "y=",y, "z=", z)

def go()
    a = 7
    foo(a, a+1)
    print("a=", a)

go()
