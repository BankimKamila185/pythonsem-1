
string = input("Enter a string: ")

palindrome = string == string[::-1]

mid = len(string) // 2
symmetrical = string[:mid] == string[mid:] if len(string) % 2 == 0 else string[:mid] == string[mid+1:]

print(f"The string '{string}' is {'a palindrome' if palindrome else 'not a palindrome'} and {'symmetrical' if symmetrical else 'not symmetrical'}.")
