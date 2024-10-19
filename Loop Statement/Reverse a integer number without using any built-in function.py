number = int(input("Enter an integer: "))
reversed_number = 0
while number:
    reversed_number = reversed_number * 10 + number % 10
    number //= 10
print(f"Reversed number is: {reversed_number}")
