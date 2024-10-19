def union_and_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    union_result = list(set1.union(set2))
    
    intersection_result = list(set1.intersection(set2))
    
    return union_result, intersection_result

# Example usage:
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

union, intersection = union_and_intersection(list_a, list_b)
print("Union:", union)
print("Intersection:", intersection)
