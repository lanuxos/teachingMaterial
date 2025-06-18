# arithmetic_infinity
while True:
    first = float(input('Please enter first value >_ '))
    second = str(input('Please enter + - * / operator >_ '))
    third = float(input('Please enter second value >_ '))
    if second == '+':
        print(first + third)
    elif second == '-':
        print(first - third)
    elif second == '*':
        print(first * third)
    elif second == '/':
        print(first / third)
