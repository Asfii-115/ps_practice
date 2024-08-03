def without_end(str):
    length = len(str)
    if length > 3:
        return str[1 : length - 1]
    else:
        return str


print(without_end("cod"))
