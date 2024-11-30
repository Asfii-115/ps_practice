def char_count(s):
    count = {}
    for x in s:
        if x not in count:
            count[x] = 0
        count[x] += 1
    return count


def most_frequent_char(s):
    cc = char_count(s)
    max_value = 0
    max_char = ""
    for x, y in cc.items():
        if y > max_value:
            max_value = y
            max_char = x
    return max_char


print(most_frequent_char("potato"))


print(char_count("bookeeper"))


def mfc(s):
    li = list(set(s))
    max_f = ""
    count = 0
    for x in li:
        if s.count(x) > count:
            max_f = x
            count = s.count(x)
    return max_f


print(mfc("bookeeper"))


def mfc2(s):
    count = {}
    for x in s:
        if x not in count:
            count[x] = 0
        count[x] += 1

    best = None
    for x in count:
        if best is None or count[x] > count[best]:
            best = x
    return best


print(mfc2("potato"))
