str1 = input()
str2 = input()

length1 = 0
length2 = 0

for i in str1:
    length1 += 1

for i in str2:
    length2 += 1

# write your code here
if length1 == length2 and str1==str2:
    print('Yes') 
else:
    print('No')
