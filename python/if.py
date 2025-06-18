# if
occupy = input('Please enter your occupy (student/teacher)')

if occupy.lower() == 'student':
    print('Keep studying...')

# if-else
weather_condition = input('Is it rain? (yes/no) >_ ')

if weather_condition.lower() == 'yes':
    print('Take a rain coat')
else:
    print('Bring an umbrella')

# if-elif-else
score = float(input('Please enter your score >_ '))

if score >= 80:
    print('Good job')
elif score >= 50:
    print('Pass')
else:
    print('Fail')
