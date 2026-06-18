a1 = int(input('Enter angle of 1 side: '))
a2 = int(input('Enter angle of 2 side: '))
a3 = int(input('Enter angle of 3 side: '))
if(a1+a2>a3 and a1+a3>a2 and a2+a3>a1):
    print('Triangle is valid')
else:
    print('Triangle is not valid')