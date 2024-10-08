# def plusone(digits):
#     n = len(digits)
#     if digits[-1] == 9:
#         if n == 1:
#             return [1, 0]
#         return digits[:-1] + [0]
#     else:
#         digits[-1] += 1
#     return digits


# print(plusone([1, 2, 9]))


def containsDuplicate(nums):
    for x in range(len(nums)):
        if nums[x] in nums[x + 1 :]:
            return True
    return False


print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
