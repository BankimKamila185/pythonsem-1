def calculate_electricity_bill(units):
    if units <= 100:
        bill = 0
    elif units <= 200:
        bill = (units - 100) * 5
    else:
        bill = (100 * 5) + (units - 200) * 10

    return bill

units = int(input("Enter the number of units consumed: "))
bill = calculate_electricity_bill(units)
print(f"The electricity bill is: Rs {bill}")

