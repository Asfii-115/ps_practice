# def big_diff(nums):
#     return max(nums) - min(nums)


# print(big_diff([10, 3, 5, 6]))
def centered_average(nums):
    max_n = max(nums)
    min_n = min(nums)
    return (sum(nums) - (max_n + min_n)) // (len(nums) - 2)


print(centered_average([-10, -4, -2, -4, -2, 0]))
