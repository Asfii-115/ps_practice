s = input()
s.lower()
z_count = s.count("z")
o_count = s.count("o")
if 2 * z_count == o_count:
    print("Yes")
else:
    print("No")
