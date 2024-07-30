string = input()
mid = len(string) // 2
if len(string) % 2 == 0:
    if string[mid:] == string[:mid]:
        print("It is a symmetry")
    else:
        print("not a symmetry")
else:
    print("can not be a symmetry")

reverse_str = string[::-1]

if reverse_str == string:
    print("also a pallindrome")
else:
    print("not a pallindrome")

# def is_pali(s):
#   return s == s[::-1]

# def is_suym(s):
#   mid =len(s)//2
#   return s[:mid] == s[-mid:] #first part == last part
