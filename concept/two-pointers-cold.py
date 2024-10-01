def reverse_list(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr


print(reverse_list([1, 2, 3, 4, 5]))


def remove_duplicate(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return arr


print(remove_duplicate([1, 1, 2, 2, 3, 4]))


def remove_duplicates(arr):
    if not arr:  # Check if the array is empty
        return 0

    i = 0  # Pointer i will track the position of the last unique element

    for j in range(1, len(arr)):  # Start from the second element
        if arr[j] != arr[i]:  # If a new unique element is found
            i += 1  # Move the i pointer
            arr[i] = arr[j]  # Update the array at index i

    # The new length of the array with unique elements is i + 1
    return arr


# Test the function
print(remove_duplicates([1, 1, 2, 2, 3, 4]))
