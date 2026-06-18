a = int(input('Enter 1st subject marks: '))
b = int(input('Enter 2nd subject marks: '))
c = int(input('Enter 3rd subject marks: '))
d = int(input('Enter 4th subject marks: '))
e = int(input('Enter 5th subject marks: '))

total = a + b + c + d + e
percentage = (total / 500) * 100
if(percentage >= 90):
    print('First Class')
elif(percentage >= 70):
    print('Second Class')
elif(percentage >= 50):
    print('Third Class')
elif(percentage >= 40):
    print('Pass')
else:
    print('Fail')