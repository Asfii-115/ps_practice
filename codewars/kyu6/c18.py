from collections import Counter
def highest_rank(arr):
    count = Counter(arr)
    max_f = max(count.values())
    mfv = [x for x,y in count.items() if y==max_f]
    return count.items()
print(highest_rank([1,1,1,2,3,4,1]))
