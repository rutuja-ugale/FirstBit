# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input('Enter Your Gender(M/F): ')
age = int(input('Enter Your Age: '))

if(gender == 'F'):
    if(age >= 18):
        print('Girl Eligible for marrige')
    else:
        print('Girl Not Eligible')
else:
    if(age >= 21):
        print('Boy Eligible For marrige')
    else:
        print('Boy Not Eligible')