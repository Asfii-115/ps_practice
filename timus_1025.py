n=int(input())
x=list(map(int,input().split()))
x.sort()
count = 0
for i in range(n // 2+1):
    count += (x[i] // 2) + 1
print(count)