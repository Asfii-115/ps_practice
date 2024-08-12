# def square_digits(num):
#     # Your code here
#     li = ""
#     sum = 1
#     for x in str(num):
#         sum = int(x) * int(x)
#         li += str(sum)
#     return int(li)


# print(type(square_digits(765)))


def high_and_low(numbers):
    numbers = numbers.split()
    li = []
    for x in numbers:
        li.append(int(x))

    return f"{max(li)} {min(li)}"


print(high_and_low("1 2 3 4 -5"))

# a = "1 2 3 4 -5"
# print(a.split())
