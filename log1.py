num = int(input())
temp = num
sum = 0
digits = list(str(num))
for x in digits:
  sum = sum + int(x)**3

if sum == temp:
  print('Armstrong number')
else:
  print('Not Armstrong number')  