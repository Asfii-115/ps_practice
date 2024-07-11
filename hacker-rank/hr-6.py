n = int(input())
arr = list(map(int, input().split()))[:n]
res = list(set(arr))
res.sort()
print(res[len(res)-2])