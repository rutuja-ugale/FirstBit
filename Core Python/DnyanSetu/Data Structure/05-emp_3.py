emp = {}
for i in range(3):
    print("\n Enter emp details: ")
    name = input("enter name: ")
    sal = float(input('enter salary: '))
    addr = input('enter address: ')

    emp[i]={'name': name, 'sal': sal, 'addr': addr}

print('\n ******* Employee Details ***********')

for key, val in emp.items():
    print(f"\nEmployee {key}")
    print(f'Name: {val["name"]}')
    print(f'Salary: {val["sal"]}')
    print(f'Addr: {val["addr"]}')