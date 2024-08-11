# def reverse_seq(n):
#     rev = []
#     while n > 0:
#         rev.append(n)
#         n -= 1
#     return rev


# -----------feedback
def rev_seq(n):
    return list(range(n, 0, -1))


print(rev_seq(5))
