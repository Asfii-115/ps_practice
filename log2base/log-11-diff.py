str1 = input()
rev_str = ''

str1_len = len(str1)

for x in range(str1_len):
  rev_str = str1[x]+rev_str


print(rev_str)  