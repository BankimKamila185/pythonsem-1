
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)

sum_tuple = tuple(a + b + c for a, b, c in zip(tuple1, tuple2, tuple3))

print("Original tuples:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Tuple 3:", tuple3)
print("Element-wise sum of the said tuples:", sum_tuple)
