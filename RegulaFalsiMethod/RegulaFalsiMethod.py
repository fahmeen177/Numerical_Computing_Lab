# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:21:02 2020

@author: user
"""

# Defining Function
def f(x):
    return (x*x*x)-(4*x)+1

# Implementing Regula Falsi Method
def regulaFalsi(x0,x1,e):
    step = 1
    print('\n\n*** REGULA FALSI IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration=%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired root is: %0.8f' % x2)


# Input Section
x0 = input('First Guess: ')
x1 = input('Second Guess: ')
e = input('Tolerable Error: ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

# Checking Correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root!')
    print('Try Again with different guess values!')
else:
    regulaFalsi(x0,x1,e)