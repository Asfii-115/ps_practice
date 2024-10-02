def c(nums, val):
    count = 0
    for x in range(len(nums)):
        if nums[x] != val:

            count += 1
    return count


print(c([0, 1, 2, 2, 3, 0, 4, 2], 2))
