
n_terms = 10

n1, n2 = 0, 1
count = 0

print("Fibonacci sequence up to 10 terms:")
while count < n_terms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
