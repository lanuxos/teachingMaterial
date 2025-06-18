# module

# import module
import random
print('RANDOM FLOATING POINT 0-1:', random.random())
print('RANDOM BETWEEN([START STOP[ STEP): ', random.randrange(1, 100))

# from module import function
from random import randint
print('RANDOM INT([START STOP] NO_STEP):', randint(1,100))

from math import sqrt, pow, pi, cos, sin, tan
print('SQUARE ROOT: ', sqrt(9))
print('2 POWER 3: ', pow(2, 3))
print('PI: ', pi)
print('COSINE: ', cos(120))

# import module as new_module
from statistics import mean as me
number_list = [1,2,3,4,5]
print('MEAN: ', me(number_list))

# user-defined module
import my_intro
my_intro.self_info()

from my_intro import self_skill, self_work, self_tel
self_skill('JS')
self_work()
self_tel()