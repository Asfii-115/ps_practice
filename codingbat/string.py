def front_back(str):
    last = len(str)
    return str[-1:] + str[1 : last - 1] + str[0]


print(front_back("asfi"))


def front_back(str):
    if len(str) <= 1:
        return str
    last = len(str) - 1
    return str[last] + str[1:last] + str[0]
