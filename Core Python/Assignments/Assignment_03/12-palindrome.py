num = int(input('Enter 3 digit number: '))
temp = num
d1 = temp % 10
temp = temp // 10

d2 = temp % 10
temp = temp // 10

d3 = temp % 10
sum = d1 * 100 + d2 * 10 + d3
if(num == sum):
    print(num, 'is a palindrome number.')
else:
    print(num, 'is not a palindrome number.')