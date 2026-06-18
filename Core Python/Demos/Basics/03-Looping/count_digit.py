num = int(input('Enter a number:'))
temp = num
count = 0
while(num > 0):
    num = num // 10
    count += 1
print(count)