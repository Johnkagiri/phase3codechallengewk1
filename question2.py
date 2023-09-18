def remove_duplicates(sequence):
    # Initialize an empty set to store unique elements
    unique_set = set()
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate through the sequence
    for item in sequence:
        # If the item is not in the unique_set, add it to both the set and the result list
        if item not in unique_set:
            unique_set.add(item)
            result.append(item)
    
    return result

# Test case
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]