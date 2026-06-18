num = int(input("Enter a three-digit number: "))
d3 = num % 10
num = num // 10

d2 = num % 10
d1 = num // 10

reverse = (d3 * 100) + (d2 * 10) + d1
print('Reversed number is: ', reverse)