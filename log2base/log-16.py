arr = []
size = int(input())

for i in range(size):
    i = int(input())
    arr.append(i)

# write your code here
even_count = 0
odd_count = 0
for x in arr:
    if x % 2 == 0:
        even_count += 1  # even
    else:
        odd_count += 1

print("Even Number Count = ", even_count)
print("Odd Number Count = ", odd_count)
