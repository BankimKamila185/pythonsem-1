char = input("Enter an alphabet: ")

if char.isalpha() and len(char) == 1:
    print(f"{char} is a {'vowel' if char in 'aeiouAEIOU' else 'consonant'}.")
else:
    print("Please enter a single alphabet character.")


