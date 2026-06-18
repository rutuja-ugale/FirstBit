cost_price = float(input("Enter the cost price: "))
discount = float(input("Enter the discount percentage: "))

discount_amt = cost_price * (discount / 100)
selling_price = cost_price - discount_amt


print(f'The selling price is: {selling_price}')
print(f'The discount amount is: {discount_amt}')