str1 = input()
length = len(str1)
newstr = ""

# for i in range(length):
#     if (str1[i] >= 'a') and (str1[i] <= 'z'):
#         newstr = newstr + chr(ord(str1[i]) - 32)
#     elif (str1[i] >= 'A') and (str1[i] <= 'Z'):
#         newstr = newstr + chr(ord(str1[i]) + 32)

# print(newstr)

for i in range(length):
    if str1[i] >= "a" and str1[i] <= "z":
        newstr += chr(ord(str1[i]) - 32)
    elif str1 >= "A" and str1[i] <= "Z":
        newstr += chr(ord(str1[i]) + 32)
print(newstr)
