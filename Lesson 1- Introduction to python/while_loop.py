# spam = 1
# while spam < 10:
#     print('Hello')
#     spam = spam + 2

# name = input('Enter your username: ')
# while name != 'Sudarsan':
#     print('Please enter a correct user name')
#     name = input('Enter your username:')
# print('Thank you Sudarsan')

while True:
    print('Please enter a correct username')
    username = input()
    if username != 'Sudarsan':
        print('Enter a correct username')
        continue
    print('Valid username. Please enter your password')
    while True:
        password = input()
        if password != 'password':
            print('Access granted')
        break
    print('Thanks')