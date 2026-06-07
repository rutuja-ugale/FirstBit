p = int(input('Enter Principal Amount: '))
r = float(input('Enter Rate Of Interest: '))
t = int(input('Enter Time (in years): '))

ci = p * (1 + r / 100) ** t - p

print(f'Compound Interest: {ci}')