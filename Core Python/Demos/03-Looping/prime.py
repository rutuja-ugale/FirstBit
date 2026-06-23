num = int(input('Enter Number: '))
for i in range(2,num):
    if (num % i) == 0:
        print(num, 'prime')
        break
    else:
        print('Not')
        break
else:
    print('Not')