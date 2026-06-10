gender = input('Enter Gender(M/F): ')
age = int(input('Enter Age: '))

if(gender == 'F'):
    if(age >= 18):
        print('Girl Eligible For Marrige')
    else:
        print('Pehle bde ho jao..')
else:
    if(age >= 21):
        print('Boy Eligible for marrige')
    else:
        print('Pehle kma lo...')