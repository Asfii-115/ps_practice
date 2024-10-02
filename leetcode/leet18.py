def search(nums, t):
    for x in range(len(nums)):
        if nums[x] == t:
            return x
        # Ensure x+1 is a valid index before accessing nums[x+1]
        elif x < len(nums) - 1 and t > nums[x] and t < nums[x + 1]:
            return x + 1
    # If the target is greater than all elements, return the length of the list
    return x + 1


print(search([1, 3, 5, 6], 8))
