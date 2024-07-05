def chk_pali(s):
  r=s[::-1]
  if r==s:
    return True
    # print('it is a pallindrome')
  return False


print(chk_pali('wow'))
# s='asfi'
# print(s[::-1])
