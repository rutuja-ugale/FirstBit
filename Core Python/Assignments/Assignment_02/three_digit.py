num = int(input('Enter a three-digit number: '))
d3 = num % 10
num = num // 10
d2 = num % 10
num = num // 10
d1 = num
sum = d1 + d2 + d3
print(f'The sum of the digits {d1}{d2}{d3} is: {sum}')