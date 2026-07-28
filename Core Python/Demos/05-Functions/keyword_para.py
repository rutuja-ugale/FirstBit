def emp(id, name, sal, dept):
    data = f'Id: {id} \nName: {name} \nSalary: {sal} \nDepartment: {dept}'
    return data
res = emp(101, sal = 50000, name = 'Rutuja', dept = 'IT')
print(res)