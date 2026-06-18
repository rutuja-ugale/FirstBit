amt = int(input('Enter the amount: '))
n1 = amt // 500
t1 = amt % 500
print(f'Number of 500 rupees notes: {n1}')
n2 = t1 // 200
t2 = t1 % 200
print(f'Number of 200 rupees notes: {n2}')
n3 = t2 // 100
t3 = t2 % 100
print(f'Number of 100 rupees notes: {n3}')
n4 = t3 // 50
t4 = t3 % 50
print(f'Number of 50 rupees notes: {n4}')
n5 = t4 // 20
t5 = t4 % 20
print(f'Number of 20 rupees notes: {n5}')
n6 = t5 // 15
t6 = t5 % 15
print(f'Number of 15 rupees notes: {n6}')
n7 = t6 // 10
t7 = t6 % 10
print(f'Number of 10 rupees notes: {n7}')
n8 = t7 // 5
t8 = t7 % 5
print(f'Number of 5 rupees notes: {n8}')
