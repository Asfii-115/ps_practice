# s = input()
# s.lower()
# z_count = s.count("z")
# o_count = s.count("o")
# if 2 * z_count == o_count:
#     print("Yes")
# else:
#     print("No")


# n = int(input())
# ans = 1
# for x in range(1, n + 1):
#     ans *= x
# print(ans)


def sum_dig_pow(a, b):
    li = []
    power = len(str(a))
    while a > 0:
        digit = a % 10
        p = digit**power
        li.append(p)
        a //= 10
        power -= 1
    return li


print(sum_dig_pow(123, 5))


def su(a, b):
    for x in range(a, b + 1):
        for i in range(1, len(str(x)) + 1):
            int(str(x)[i]) ** i


def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


print(is_prime(713))


def char_count(s):
    count = {}
    for x in s:
        if x not in count:
            count[x] = 0
        count[x] += 1
    return count


print(char_count("catss"))
