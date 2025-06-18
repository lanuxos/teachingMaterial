print('Welcome to Python Programming 101')

user_name = input("Please enter your name...\n")

print('Hi, ' + user_name + ' How are you today?')

user_response = input("fine or good or bad\n")
# check user response for choosing condition to reply
if user_response.lower() == 'fine':
    print('Well, good to hear you are FINE,\
    what can i help you to make your day better?')
elif user_response.lower() == 'good':
    print('Very well, sir. Great to know that your day\'s GOOD')
elif user_response.lower() == 'bad':
    print('I\'m so sorry to hear that,\
    how could I help you sir?')
else:
    print('I\'m not sure your answer, but hope your day is great')
