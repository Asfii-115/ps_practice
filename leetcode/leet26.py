def max(nums):
    m = 0
    m2 = 0
    m3 = 0
    for x in range(len(nums)):
        if nums[x] > m:
            m = nums[x]
    for x in range(len(nums)):
        if nums[x] > m2 and nums[x] < m:
            m2 = nums[x]
    for x in range(len(nums)):
        if nums[x] > m3 and nums[x] < m2:
            m3 = nums[x]
    return m if len(nums) <= 2 else m3


print(max([1, 2]))
