start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Print all prime numbers within the range
print([num for num in range(start, end + 1) if is_prime(num)])