"""DESCRIPTION:
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))"""

def zero(f = None): #your code here
    return 0 if f is None else f(0)
def one(f = None): #your code here
    return 1 if f is None else f(1)
def two(f = None): #your code here
    return 2 if f is None else f(2)
def three(f = None): #your code here
    return 3 if f is None else f(3)
def four(f = None): #your code here
    return 4 if f is None else f(4)
def five(f = None): #your code here
    return 5 if f is None else f(5)
def six(f = None): #your code here
    return 6 if f is None else f(6)
def seven(f = None): #your code here
    return 7 if f is None else f(7)
def eight(f = None): #your code here
    return 8 if f is None else f(8)
def nine(f = None): #your code here
    return 9 if f is None else f(9)

def plus(a): #your code here
        return lambda b: b+a
def minus(a): #your code here
        return lambda b: b-a
def times(a): #your code here
        return lambda b: b*a
def divided_by(a): #your code here
        return lambda b: b//a
