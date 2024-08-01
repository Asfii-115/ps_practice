str1 = input()
reverse_str1 = ""
length = len(str1)

for x in range(length):
    reverse_str1 = str1[x] + reverse_str1
print(reverse_str1)
