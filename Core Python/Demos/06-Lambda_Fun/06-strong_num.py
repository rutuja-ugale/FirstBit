from math import factorial
data = range(1, 1001)
res = list(filter(lambda x: sum(factorial(int(i)) for i in str(x)) == x, data))
print(res)