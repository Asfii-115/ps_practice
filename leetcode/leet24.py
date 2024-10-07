def codds(low, high):
    if low % 2 != 0:
        return len(range(low, high + 1, 2))
    return len(range(low + 1, high, 2))


print(codds(8, 10))


def countOdds(low: int, high: int) -> int:
    nums = (high - low) // 2
    return nums if low % 2 == 1 or high % 2 == 1 else nums


print(countOdds(3, 7))
