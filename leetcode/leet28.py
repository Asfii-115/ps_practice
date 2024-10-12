# def movezero(nums):
#     slow = 0
#     for x in range(1, len(nums)):
#         if nums[slow] == 0 and nums[x] != 0:
#             nums[slow], nums[x] = nums[x], nums[slow]

#         if nums[slow] != 0:
#             slow += 1
#     return nums


# print(movezero([0, 1, 0, 3, 12]))


def rev_string(s):
    i = 0
    j = len(s) - 1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

    return s


print(rev_string(["H", "a", "n", "n", "a", "h"]))
