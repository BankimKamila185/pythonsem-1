cost_price = float(input("Enter the cost price of the bike in Rs: "))

if cost_price > 100000:
    tax = cost_price * 0.15
elif cost_price > 50000:
    tax = cost_price * 0.10
else:
    tax = cost_price * 0.05
print(f"The road tax to be paid is Rs: {tax:.2f}")

