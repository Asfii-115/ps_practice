def find_it(seq):
    return [x for x in seq if seq.count(x) % 2 == 1][-1]


print(find_it([1, 1, 2]))


def duplicate_encode(word):
    # your code
    s = ""
    word = word.lower()
    for x in word:
        if word.count(x) > 1:
            s += ")"
        else:
            s += "("
    return s


print(duplicate_encode("Success"))
