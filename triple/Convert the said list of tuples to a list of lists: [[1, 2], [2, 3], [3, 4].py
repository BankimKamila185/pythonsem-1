
tuples_list = [(1, 2), (2, 3), (3, 4)]

lists_list = [list(t) for t in tuples_list]

print("Original list of tuples:", tuples_list)
print("Converted list of lists:", lists_list)
