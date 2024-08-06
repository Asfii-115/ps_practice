# def sum67(nums):
#     x = 0
#     i = 0
#     while i < len(nums):
#         if nums[i] == 6:

#             while nums[i] != 7:
#                 i += 1
#         else:
#             x += nums[i]
#             i += 1
#     return x - 7


# print(sum67([1, 2, 2, 6, 99, 99, 7]))


def sum67(nums):
    total = 0
    in_section = False

    for num in nums:
        if num == 6:
            in_section = True
        elif in_section:
            if num == 7:
                in_section = False
        else:
            total += num

    return total


# Test cases
print(sum67([1, 2, 2]))  # Should return 5
print(sum67([1, 2, 2, 6, 99, 99, 7]))  # Should return 5
print(sum67([1, 1, 6, 7, 2]))  # Should return 4
print(sum67([6, 7, 6, 7, 6, 7]))  # Should return 0
print(sum67([1, 6, 2, 2, 7, 1, 2, 7]))  # Should return 4
print(sum67([]))  # Should return 0
