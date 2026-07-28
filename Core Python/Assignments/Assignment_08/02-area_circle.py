import math
def calculateArea(radius):
    return math.pi * radius * radius
radius = float(input("Enter the radius: "))
res = calculateArea(radius)
print(res)