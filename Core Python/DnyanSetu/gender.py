gender = input('Enter Gender(M/F): ')

if(gender == 'F'):
    age = int(input('Enter Age: '))
    if(age >= 18):
        print('Girl Eligible For Marrige')
    else:
        print('Pehle bde ho jao..')
elif(gender == 'M'):
    age = int(input('Enter Age: '))
    if(age >= 21):
        print('Boy Eligible for marrige')
    else:
        print('Pehle kma lo...')
else:
    print('Invalid Gender')