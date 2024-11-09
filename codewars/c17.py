def duplicate_count(text):
    text = text.lower()  # Convert text to lowercase to handle case insensitivity
    seen = set()  # To track already counted characters
    duplicates = set()  # To track duplicates found

    for char in text:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)

    return len(duplicates)


# Test the function
print(duplicate_count("aabbcde"))  # Expected output: 2
