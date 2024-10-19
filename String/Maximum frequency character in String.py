string = input("Enter a string: ")
frequency = {}
for char in string:
    frequency[char] = frequency.get(char, 0) + 1
max_char = max(frequency, key=frequency.get)
print("The character '{}' has the highest frequency of {}.".format(max_char, frequency[max_char]))
