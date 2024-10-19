# def remove_duplicates(nums):
#     i = 0
#     for x in range(1, len(nums)):
#         if nums[i] != nums[x]:
#             i += 1
#             nums[i] = nums[x]
#     return i + 1


# print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


def remove_element(nums, val):
    count = 0
    for x in range(len(nums)):
        if nums[x] != val:
            count += 1
    return count


print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
