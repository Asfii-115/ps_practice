def move(l):
    L = sorted(l)
    c = l.count(0)
    return L[c:] + L[:c]


print(move([0, 1, 0, 3, 12]))


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

        return nums
