string = 'google.com'
frequency = {}
for char in string:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)

