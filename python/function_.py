# Python Function

def call_me(my_name):
    print('My name is', my_name)

call_me('Steve')
call_me('Jobs')

def add_two_number(num1, num2):
    result = num1 + num2
    return result

plus1 = add_two_number(1, 2)
print('Plus1 is: ', plus1)
print('Print add_two_number function result: ', add_two_number(5, 5))

def minus_two_number(num1=2, num2=1):
    return num1 - num2

print('minus function with arg:', minus_two_number(5, 3))
print('minus function with arg:', minus_two_number(1, 5))
print('minus function with arg:', minus_two_number(num2=1, num1=5))
print('minus function without arg:', minus_two_number())

# function argument types
def require_argument(first, second):
    print(first, second)

require_argument('first', 2)
require_argument(2, 'first')
# require_argument('first')

def keyword_argument(my_name, my_tel):
    print('My name is:', my_name)
    print('My phone number is:', my_tel)

keyword_argument(my_name='La', my_tel=12345678)
keyword_argument(my_tel=98765432, my_name='LA')

def default_argument(my_name='default_name'):
    print('my name is:', my_name)

default_argument(my_name='LA')
default_argument('LA')
default_argument()

def default_argument_none(first, second=None):
    print(first, second)

default_argument_none('second', 2)
default_argument_none('first')
# default_argument_none()

def variable_length_argument(*arg):
    # print(type(arg)) # tuple
    for v in arg:
        print(v)

variable_length_argument('Name: La', 'Tel: 123', 1234567890)

# anonymous function
# lambda function
return_result = lambda first, second: first + second
print('lambda_function', return_result(1, 2))

def return_result(first, second):
    return first - second
print('lambda_function_first', return_result(2, 2))

list_var = [1, 2, 3]
new_list_var = list(map(lambda x:x*2, list_var))
print('Old List:', list_var)
print('New List:', new_list_var)

another_list_var = [1, 2, '3']
newer_list_var = list(filter(lambda x:type(x)==str, another_list_var))
print('Old List Member:', another_list_var)
print('New String Member:', newer_list_var)