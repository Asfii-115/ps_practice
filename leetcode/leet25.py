def avg_sal(arr):
    sum_ = sum(arr) - max(arr) - min(arr)
    return sum_ / (len(arr) - 2)


print(avg_sal([1000, 2000, 3000]))
