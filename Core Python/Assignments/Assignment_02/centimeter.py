feet = int(input("Enter the number of feet: "))
inches = int(input("Enter the number of inches: "))
total_inches = (feet * 12) + inches

total_centimeters = total_inches * 2.54

meters = total_centimeters // 100
centimeters = total_centimeters % 100
print("Total length in meters: ", meters)
print("Total length in centimeters: ", centimeters)