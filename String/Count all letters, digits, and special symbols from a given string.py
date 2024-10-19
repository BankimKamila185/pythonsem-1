string = input("Enter a string: ")
letters = 0
digits = 0
special = 0
for char in string:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1
print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Special symbols: {special}")
