# def digitize(n):
#   a = str(n)
#   return [int(x) for x in a[::-1]]

# def digitize(n):
#     return map(int, str(n)[::-1])

# print(digitize(3242))
# def digitize(n):
#     result = []
#     while n >= 1:
#         result.append(n%10)
#         n //= 10
#     return result


def paperwork(n, m):
    if n > 0 and m > 0:
        return n * m
    return 0


def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0


def paperwork(n, m):
    return max(n, 0) * max(m, 0)


print(paperwork(-3, 5))
