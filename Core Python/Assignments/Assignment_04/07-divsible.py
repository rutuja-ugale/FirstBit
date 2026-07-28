n = int(input("Enter the number: "))
for n in range(1, n):
    if(n % 2 != 0 and n % 3 != 0):
        print(n)