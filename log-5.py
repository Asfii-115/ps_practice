num = int(input())

a = 0
b = 1

for x in range(num):
    c = a + b
    print(a)
    a = b
    b = c