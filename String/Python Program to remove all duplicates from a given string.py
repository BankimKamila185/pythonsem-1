string = input("Enter a string: ")
result = ""
for char in string:
    if char not in result:
        result += char

print(f"The string after removing duplicates: {result}")


