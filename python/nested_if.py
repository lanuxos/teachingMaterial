# nested if

gender = input('Please enter m for male or f for female >_ ')
age = int(input('Please enter your age >_ '))

if gender.lower() == 'm':
    if age >= 60:
        print('You should stay home')
    else:
        print('You should go to work!')
elif gender.lower() == 'f':
    if age >= 55:
        print('You should stay home')
    else:
        print('You should go to work!')

'''
gender = input('Please enter m for male or f for female >_ ')
day = input('Please enter day [mon, tue, wed, thur, fri, sat, sun] >_ ')

if gender.lower() == 'm':
    if day.lower() == 'mon':
        print('Taking a bath and go to school')
    elif day.lower() == 'tue':
        print('Taking a bath and go to school')
    elif day.lower() == 'wed':
        print('Taking a bath and go to school')
    elif day.lower() == 'thur':
        print('Taking a bath and go to school')
    elif day.lower() == 'fri':
        print('Taking a bath and go to school')
    else:
        print('You can stay in bed')
elif gender.lower() == 'f':
    if day.lower() == 'mon' or\
       day.lower() == 'tue' or\
       day.lower() == 'wed' or\
       day.lower() == 'thur' or\
       day.lower() == 'fri':
        print('Taking a bath, make up and go to school')
    else:
        print('You can stay in bed')
'''
