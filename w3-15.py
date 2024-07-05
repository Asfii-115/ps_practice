def sort_hyphen_sequence(input_string):
    # Split the input string by hyphens to get a list of words
    words = input_string.split('-')
    
    # Sort the list of words alphabetically
    words.sort()
    
    # Join the sorted words back into a hyphen-separated string
    sorted_string = '-'.join(words)
    
    return sorted_string

# Accept input from the user
input_string = input("Enter a hyphen-separated sequence of words: ")

# Get the sorted hyphen-separated sequence
sorted_sequence = sort_hyphen_sequence(input_string)

# Print the sorted sequence
print(sorted_sequence)
