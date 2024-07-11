def multi(num):
  total = 1
  for x in num:
    total*=x
  return total

print(multi((8,4,2)))