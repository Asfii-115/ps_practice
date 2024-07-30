test_str = "geeksforgeeks 33 is   best"
a = test_str.split()
print(a)
# res = sum(not x.isspace() for x in test_str)
res = sum(map(len, test_str.split()))
print(res)

res = test_str.replace(" ", "")
length = len(res)
print("", length)
