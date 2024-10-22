# # # # def remove_duplicates(nums):
# # # #     i = 0
# # # #     for x in range(1, len(nums)):
# # # #         if nums[i] != nums[x]:
# # # #             i += 1
# # # #             nums[i] = nums[x]
# # # #     return i + 1


# # # # print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


# # # # def remove_element(nums, val):
# # # #     count = 0
# # # #     for x in range(len(nums)):
# # # #         if nums[x] != val:
# # # #             count += 1
# # # #     return count


# # # # print(remove_element([0, 1, 2, 2, 3, 0, 4, 2],2))


# # # def merge_sorted(nums1, nums2):
# # #     i = 0
# # #     j = 0
# # #     while i < len(nums1):
# # #         if nums1[i] <= nums2[j]:
# # #             i += 1
# # #         else:
# # #             nums1[i] = nums2[j]
# # #             j += 1
# # #     return nums1


# # # print(merge_sorted([1, 2, 3, 7, 8], [2, 5, 6]))


# # def roman(s):
# #     m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# #     ans = 0
# #     for x in range(len(s)):
# #         if x < len(s) - 1 and m[s[x]] < m[s[x + 1]]:
# #             ans -= m[s[x]]
# #         ans += m[s[x]]
# #     return ans


# # print(roman("LVIII"))


# # def long(arr):
# #     li = ""
# #     v = sorted(arr)
# #     first = v[0]
# #     last = v[-1]
# #     for i in range(min(len(first), len(last))):
# #         if first[i] != last[i]:
# #             return li
# #         li += first[i]
# #     return li


# # print(long(["flower", "flow", "flight"]))


# def isomorphic(s, t):
#     map1 = []
#     map2 = []
#     for x in s:
#         map1.append(s.index(x))
#     for y in t:
#         map2.append(t.index(y))
#     return map1 == map2


# print(isomorphic("egg", "add"))

# s = "paper"
# t = "title"
# print(s.index("p"))
# print(t.index("t"))


# def rev_vowel(s):
#     li = []
#     for x in s:
#         li.append(x)
#     for i in li:
#         if i in "AEIOUaeiou":
#             li.remove(i)
#             li.append(i)
#     return li


# print(rev_vowel("Icecreame"))


# def ransom(r, m):
#     for x in r:
#         if x in m:
#             return True
#     return False


# print(ransom("aa", "ab"))


def unique(s):
    for x in range(len(s)):
        if s.count(s[x]) == 1:
            return x


print(unique("asfiasf"))


def issub(s, t):
    c, j = 0, 0
    while c < len(s) and j < len(t):
        if s[c] == t[j]:
            c += 1
        j += 1
    return len(s) == c


print(issub("acb", "axbjc"))
