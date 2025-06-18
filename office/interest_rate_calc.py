# interestCalc.py
while 1:
    principle = float(input('\nPlease input your start principle amount >_\t'))
    rate = float(input('Please input your bank interest rate (%)>_\t'))
    duration = int(input('Please input your deposit days >_\t\t'))

    interest = principle * (rate / 100) * (duration / 365)
    net_balance = principle + (principle * (rate / 100) * (duration / 365))

    print('\nYour principle >_\t', format(principle, ',.2f'))
    print('Interest rate', rate, '% >_\t', format(rate / 100, '.2f'))
    print('Deposit duration >_\t', duration, 'day(s)')
    print('Interest you earn >_\t', format(interest, ',.2f'))
    print('Net balance >_\t\t', format(net_balance, ',.2f'))
