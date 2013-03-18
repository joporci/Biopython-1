# This program computes the sum of squares of two or three numbers

import q2_3 # this is a module that contain a function that computes the sum of squares of two or three numbers

a = int(raw_input('Enter number a: '))
b = int(raw_input('Enter number b: '))
c = int(raw_input('Enter number c: '))

print q2_3.sum_sq(a,b,c)


x = int(raw_input('Enter number x: '))
y = int(raw_input('Enter number y: '))

print q2_3.sum_sq(x,y)
