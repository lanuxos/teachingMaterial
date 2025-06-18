# variable scope

global_variable = 'This is a GLOBAL variable'

def my_function():
    local_variable = 'LOCAL variable'
    print('NO RETURN FUNCTION #_', global_variable, 'and', local_variable)

my_function()

print('NO RETURN #_', global_variable)


def my_return_function():
    local_variable = 'LOCAL variable'
    print('RETURN function >_', global_variable, 'and', local_variable)
    return local_variable

local_return = my_return_function()

print('RETURN >_', global_variable)
print('RETURN LOCAL >_', local_return)

name = 'Python'

def print_name():
    name = 'JS'
    global lastname
    lastname = 'Programming'
    print('LOCAL >>>', name)

print('GLOBAL >>>', name)
print_name()
print('LOCAL AS GLOBAL >_', lastname)