# Define the string
string = "Bankim kamila "

# Define a set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Count vowels
vowel_count = len([char for char in string if char in vowels])

# Display the result
print("Number of vowels in the string:", vowel_count)
