days = int(input('Enter Number Of Days: '))
years = days // 365
days = days % 365
weeks = days // 7
days = days % 7
print(f'Years: {years}')
print(f'Weeks: {weeks}')
print(f'Days: {days}')