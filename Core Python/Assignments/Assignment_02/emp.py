basic_salary = float(input('Enter the basic salary: '))
da = 0.10 * basic_salary
ta = 0.12 * basic_salary
hra = 0.15 * basic_salary
total_salary = basic_salary + da + ta + hra
print('da: ', da)
print('ta: ', ta)
print('hra: ', hra)
print(f'The total salary is: {total_salary}')