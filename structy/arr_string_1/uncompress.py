def uncompress(s):
  numbers = '0123456789'
  res = '' #use a list instead
  i = 0
  j = 0
  while j < len(s):
    if s[j] in numbers:
      j+=1
    else:
      num = int(s[i:j])
      res+= s[j]*num
      j+=1
      i = j
  return res

print(uncompress('12t'))      


          
      