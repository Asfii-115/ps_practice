def runningSum(nums):
    result = []
    result.insert(0, nums[0])
    for x in range(1, len(nums)):
        result.append(nums[x] + nums[x - 1])
    return result


print(runningSum([1, 2, 3, 4]))
