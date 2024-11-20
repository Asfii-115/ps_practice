def numss(nums):
    l = []
    for x in range(1, len(nums) + 1):
        l.append(sum(nums[0:x]))
    return l


print(numss([1, 2, 3, 4]))


def max_wealth(accounts):
    m = 0
    for x in accounts:
        if sum(x) > m:
            m = sum(x)
    return m


print(max_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
