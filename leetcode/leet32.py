def fizzbuzz(n):
    li = []
    for x in range(1, n + 1):
        if x % 3 == 0 and x % 5 == 0:
            li.append("FizzBuzz")
        elif x % 3 == 0:
            li.append("Fizz")
        elif x % 5 == 0:
            li.append("Buzz")
        else:
            li.append(str(x))
    return li


print(fizzbuzz(3))


def nos(num):
    i = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
            i += 1
        if num % 2 == 1:
            num = num - 1
            i += 1
    return i


print(nos(14))
