# homework2

while True:
    score = float(input('Please enter your score :: '))

    if score >= 95:
        print('You get A+')
    elif score >= 90:
        print('You get A')
    elif score >= 81:
        print('You get B')
    elif score >= 71:
        print('You get C')
    elif score >= 50:
        print('You get D')
    else:
        print('You get F')
