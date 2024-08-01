arr = []
n = int(input())

for i in range(n):
    i = int(input())
    arr.append(i)

# write your code here
max = arr[0]
for x in range(n):
    if max < arr[x]:
        new_max = arr[x]

print(new_max)

# max = arr[0]

# for i in range(n):
#     if arr[i] > max:
#         max = arr[i]

# print("Max = ", max)
