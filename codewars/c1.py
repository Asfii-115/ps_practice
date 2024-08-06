# def remove_char(s):
#     return s[1 : len(s) - 1]


# print(remove_char("asfi"))

#  def square_sum(numbers):
#     #your code here


# def summation(num):
#     sum = 0
#     for x in range(num + 1):
#         sum += x
#     return sum


# print(summation(8))


def summation(num):
    return sum(x for x in range(num + 1))


print(summation(8))
