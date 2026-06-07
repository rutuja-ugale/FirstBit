a = float(input('Enter the 1 number: '))
b = float(input('Enter the 2 number: '))
c = float(input('Enter the 3 number: '))
d = b ** 2 - 4 * a * c
if d > 0:
    root1 = (-b + d ** 0.5) / (2 * a)
    root2 = (-b - d ** 0.5) / (2 * a)

if d == 0:
    root1 = root2 = -b / (2 * a)

if d < 0:
    root1 = root2 = None

print(f'Roots of the quadratic equation are: {root1} and {root2}')