a1 = int(input('Enter angle 1 side: '))
a2 = int(input('Enter angle 2 side: '))
a3 = int(input('Enter angle 3 side: '))
if(a1==a2 and a2==a3):
    print('Triangle is Equilateral')
elif(a1==a2):
    print('Triangle is Isosceles')
else:
    print('Triangle is Scalene')