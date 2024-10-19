
tuples_list = [(1, 2), (), (3, 4), (), (5, 6, 7), ()]

# Remove empty tuples
filtered_list = [t for t in tuples_list if t]

# Display the result
print("Original list of tuples:", tuples_list)
print("List after removing empty tuples:", filtered_list)
