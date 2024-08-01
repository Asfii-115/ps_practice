str1 = input()
newstr = ""
for x in str1:
    if x.isupper() == True:
        a = x.lower()
        newstr += a
    else:
        a = x.upper()
        newstr += a

print("".join(newstr))
