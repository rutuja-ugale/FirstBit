a = int(input('Enter Marks Of Subject 1: '))
b = int(input('Enter Marks Of Subject 2: '))
c = int(input('Enter Marks Of Subject 3: '))
d = int(input('Enter Marks Of Subject 4: '))
e = int(input('Enter Marks Of Subject 5: '))

total = a + b + c + d + e
per = (total / 500) * 100
print(f'Percentage: {per}%')