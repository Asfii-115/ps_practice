# def sum13(nums):
#     count = 0
#     if len(nums) < 1:
#         return 0
#     for x in range(len(nums) - 1):
#         if nums[x] == 13:
#             count += nums[x + 2]
#         else:
#             count += nums[x]
#     return count


# print(sum13([1, 2, 2, 1]))


def sum13(nums):
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2  # Skip the current number and the next one
        else:
            count += nums[i]
            i += 1  # Move to the next element
    return count


# Test case
