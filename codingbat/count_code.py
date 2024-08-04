def count_code(str):
    count = 0
    for x in range(len(str)):
        if (str[x : x + 4] == "code") or (str[x : x + 2] == "co" and str[x + 3] == "e"):
            count += 1
    return count


print(count_code("cozexxcope"))
