def xyz_there(str):
    for x in range(len(str) - 2):
        if str[x : x + 3] == "xyz":
            if x == 0 or str[x - 1] != ".":
                return True
    return False


print(xyz_there("abcxyz"))
print(xyz_there("abc.xyz"))
print(xyz_there("xyz.abc"))
