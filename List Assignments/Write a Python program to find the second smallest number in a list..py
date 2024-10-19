def find_second_smallest(numbers):
    # Step 1: Remove duplicates by converting to a set
    unique_numbers = set(numbers)
    
    # Step 2: Check if we have at least two unique numbers
    if len(unique_numbers) < 2:
        return "There is no second smallest number."
    
    # Step 3: Sort the unique numbers
    sorted_numbers = sorted(unique_numbers)
    
    # Step 4: Return the second smallest number
    return sorted_numbers[1]

# Example usage
numbers = [5, 3, 1, 4, 1, 3]
second_smallest = find_second_smallest(numbers)
print("The second smallest number is:", second_smallest)
