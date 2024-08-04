def count_hi(str):
    count = 0
    for x in range(len(str)):
        if str[x : x + 2] == "hi":
            count += 1
    return count


print(count_hi("ABChi hi"))
