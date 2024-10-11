def movezero(nums):
    slow = 0
    for x in range(1, len(nums)):
        if nums[slow] == 0 and nums[x] != 0:
            nums[slow], nums[x] = nums[x], nums[slow]

        if nums[slow] != 0:
            slow += 1
    return nums


print(movezero([0, 1, 0, 3, 12]))
