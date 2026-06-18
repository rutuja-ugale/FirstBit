import random
user = "rutuja"
passw = "rutuja123"

username = input('Enter username: ')
password = input('Enter password: ')

if(username == user and password == passw):
    captcha = random.randint(1000, 9999)
    print('Captcha: ', captcha)
    user_captcha = int(input('Enter the captcha: '))
    if(user_captcha == captcha):
        print('Login Successful!')
    else:
        print('Captcha Incorrect! Login Failed!')
else:
    print('Login Failed!')
