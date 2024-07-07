num = int(input())
result = 0
temp = num

while num:
    mod = num % 10
    result = result + mod * mod * mod
    num = num // 10

if temp == result:
    print("Armstrong number")
else:
    print("Not Armstrong number")