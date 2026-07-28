def isFactorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def isStrong(num):
    temp = num
    sum = 0
    while(temp > 0):
        d = temp % 10
        print('digit: ',d)
        temp = temp // 10

        fact = isFactorial(d)
        print("factorial: ", fact)

        sum = sum + fact
        print('sum: ', sum)

    if(num == sum):
        return True
    else:
        return False

n = 145
res = isStrong(n)
print(res)