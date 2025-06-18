# recursive function

# Factorial
def factorial_function(n):
    if n == 1:
        return 1
    else:
        factorial_result = n * factorial_function(n-1)
        return factorial_result

print('FACTORIAL FUNCTION: ', factorial_function(5))

# Exponent
def exponent_function(x, y):
    if y == 0:
        return 1
    else:
        return x * exponent_function(x, y-1)
    
print('EXPONENT FUNCTION: ', exponent_function(2, 3))

# Fibonacci
def fibonacci_function(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_function(n-1) + fibonacci_function(n-2)
    
print('FIBONACCI FUNCTION: ', fibonacci_function(10))

# sum of list
def sum_of_list(list):
    if not list:
        return 0
    return list[0] + sum_of_list(list[1:])

print('SUM OF LIST: ', sum_of_list([1,2,3,4,5]))