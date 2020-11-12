#Name: Terry Su
#Date: July 24, 2020
#Purpose: Lambda expressions / anonymous functions

#Suppose we would like to create a function to compute 3x + 1
#Standard approach (def a normal function)
print('Lambda expression example')
def f(x):
    return (3*x) + 1
print(f(5))

#It can also be done using a lambda expression

function = lambda x: (3*x) + 1
#Lambda expressions are single lined functions that return a value
#They use the keyword lambda, followed by the argument(s), a colon, and the expression
#they can be stored inside a variable and used just like a normal function
print(type(function))
print(function(5))
print()

#Lambda expressions may have multiple arguments but only one expression
print('Multiple arguments example')
full_name = lambda first,last: first.strip().title() + ' ' + last.strip().title()
print(full_name('     TERRy  ', '  su'))
print()

#Lambda expressions may also be used within a parent function
print('Lambda expression within a function example')
def quadratic(a,b,c):
    """returns the y value for a given x value in a custom expression"""
    return lambda x: a*(x**2) + b*x + c

build_quadratic = quadratic(2,3,5) #input for (a,b,c)
print(build_quadratic(3)) #input for x

#another way of getting the same result
print(quadratic(2,3,5)(3))

