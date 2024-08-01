arr = []
n = int(input())

for i in range(n):
    i = int(input())
    arr.append(i)

# write your code here
max = arr[0]
min = arr[0]
for i in range(n):
    if arr[i] > max:
        max = arr[i]

    if arr[i] < min:
        min = arr[i]

print("max=", max)
print("min=", min)
