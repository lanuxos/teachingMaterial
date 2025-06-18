# Exception handling

# try-except
a = input('Please enter a number >_ ')
b = input('Please enter a number >_ ')

try:
    int(a) / int(b)
except ZeroDivisionError:
    print('Zero Division Error')
except:
    print('Something is wrong')
else:
    print(int(a) / int(b))
finally:
    print('Done with checking error with try-except')

# # raise
# if type(a) or type(b) is str:
#     raise TypeError('Your enter string instead of number')

# # assert
# assert (int(b) != 0), 'can not divide by zero!'
# print(int(a) / int(b))
