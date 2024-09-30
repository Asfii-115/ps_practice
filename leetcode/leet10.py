def arrayone(nums):
    x = 1
    for i in nums:
        x *= i
    return 1 if x > 0 else (0 if x == 0 else -1)


print(arrayone([1, 5, 0, 2, -3]))
