# This program computes the sum of squares of two numbers.


a = int(raw_input('Enter number: '))
b = int(raw_input('Enter number: '))

import q1_3 # this is a module that contain a function that computes the sum of squares of two numbers

print q1_3.sum_sq(a, b)
