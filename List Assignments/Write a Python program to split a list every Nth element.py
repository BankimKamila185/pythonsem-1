def split_list(original_list, N):
    if N <= 0:
        raise ValueError("N must be a positive integer.")
    
    split_parts = []
    
    for i in range(0, len(original_list), N):
  
        split_parts.append(original_list[i:i + N])
    
    return split_parts

example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = 3
result = split_list(example_list, N)
print(result)
