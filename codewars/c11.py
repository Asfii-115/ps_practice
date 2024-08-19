# def number(bus_stops):
#     get_off = 0
#     get_on = 0
#     for x in bus_stops:
#         get_on += x[0]
#         get_off += x[1]
#     return get_on - get_off


# print(number([[10, 0], [3, 5], [5, 8]]))


# def odd_or_even(arr):
#     return "even" if sum(arr) % 2 == 0 else "odd"


# print(odd_or_even([0]))


# def reverse_words(text):
#     return " ".join(text[::-1].split()[::-1])


# def reverse_words(text):
# rev = ""
# for x in text:
#     rev = x + rev
# return rev
# def reverse_words(text):
#     li = []
#     for x in text.split(" "):
#         li.append(x[::-1])
#     return " ".join(li)


# print(reverse_words("This is an example!"))


def remove_smallest(numbers):
    m = min(numbers)
    numbers.remove(m)
    return numbers


print(remove_smallest([1, 2, 3, 4, 5]))
