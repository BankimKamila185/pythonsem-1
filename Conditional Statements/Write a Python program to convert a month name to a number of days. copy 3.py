marked_price = float(input("Enter the marked price in Rs: "))

if marked_price > 10000:
    discount = marked_price * 0.20
elif marked_price > 7000:
    discount = marked_price * 0.15
else:
    discount = marked_price * 0.10

net_amount = marked_price - discount

print(f"The net amount to be paid is Rs: {net_amount:.2f}")


