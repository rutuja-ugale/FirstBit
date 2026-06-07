p = int(input('Enter Principal Amount: '))
t = int(input('Enter Time (in years): '))
r = float(input('Enter Rate Of Interest: '))
si = (p * t * r) / 100
a = p + si
print(f'Simple Interest: {a}')