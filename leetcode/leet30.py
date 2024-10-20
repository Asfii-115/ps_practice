# # def remove_duplicates(nums):
# #     i = 0
# #     for x in range(1, len(nums)):
# #         if nums[i] != nums[x]:
# #             i += 1
# #             nums[i] = nums[x]
# #     return i + 1


# # print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


# # def remove_element(nums, val):
# #     count = 0
# #     for x in range(len(nums)):
# #         if nums[x] != val:
# #             count += 1
# #     return count


# # print(remove_element([0, 1, 2, 2, 3, 0, 4, 2],2))


# def merge_sorted(nums1, nums2):
#     i = 0
#     j = 0
#     while i < len(nums1):
#         if nums1[i] <= nums2[j]:
#             i += 1
#         else:
#             nums1[i] = nums2[j]
#             j += 1
#     return nums1


# print(merge_sorted([1, 2, 3, 7, 8], [2, 5, 6]))


def roman(s):
    m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0
    for x in range(len(s)):
        if x < len(s) - 1 and m[s[x]] < m[s[x + 1]]:
            ans -= m[s[x]]
        ans += m[s[x]]
    return ans


print(roman("LVIII"))


def long(arr):
    li = ""
    v = sorted(arr)
    first = v[0]
    last = v[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return li
        li += first[i]
    return li


print(long(["flower", "flow", "flight"]))
