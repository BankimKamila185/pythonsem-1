# Get the string from the user
user_input = input("Enter a string: ")
digit_count = sum(char.isdigit() for char in user_input)
letter_count = sum(char.isalpha() for char in user_input)

# Display the results
print(f"Number of letters: {letter_count}")
print(f"Number of digits: {digit_count}")
