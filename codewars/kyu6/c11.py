import math


def comp(array1, array2):
    c = 0
    for x in array2:
        if math.sqrt(x) in array1:
            c += 1
    return c == len(array1)


print(
    comp(
        [121, 144, 19, 161, 19, 144, 19, 11],
        [121, 14641, 20736, 36100, 25921, 361, 20736, 361],
    )
)
