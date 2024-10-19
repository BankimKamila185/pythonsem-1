def remove_duplicates(input_list):

    unique_set = set(input_list)
    
    # Convert the set back to a list
    unique_list = list(unique_set)
    
    return unique_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 4, 5, 6, 1, 2]
    print("Original List:", my_list)
    result = remove_duplicates(my_list)
    print("List after removing duplicates:", result)
