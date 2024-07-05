def find_factorial(n):
  total =1
  for x in range(1,n+1):
    total*=x
  return total

print(find_factorial(3))