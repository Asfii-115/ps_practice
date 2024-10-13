# def string_score(s):
#     count = 0
#     for x in range(1, len(s)):
#         count += abs(ord(s[x]) - ord(s[x - 1]))
#     return count


# print(string_score("hello"))


def cal(operations):
    li = []
    for x in operations:
        if x != "C" or x != "D":
            li.append(int(x))
        if x == "D":
            li.append(x)
        else:
            li.append(x)
    return li


print(cal(["5", "2", "C", "D", "+"]))
