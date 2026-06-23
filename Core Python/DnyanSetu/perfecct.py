num = int(input('Enter the number: '))
sumDivisor = 0
for i in range(1, num):
    if num % i == 0:
        sumDivisor = sumDivisor + i
if sumDivisor == num:
    print('Perfect')
else:
    print('Not Perfect')