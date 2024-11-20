def longest_consec(strarr, k):
    li = []
    maxa = strarr[0]
    for x in range(len(strarr) - 1):
        i = "".join(strarr[x : k + x])
        li.append(i)
        if len(i) > len(maxa):
            maxa = i
    return maxa


print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k=2))
