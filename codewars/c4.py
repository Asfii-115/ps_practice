# def invert(lst):
#     return [-x for x in lst]


# print(invert([1, -2, 3, -4, 5]))

# string = "asfi"
# print(len(string))


def get_count(sentence):
    count = 0
    for x in range(len(sentence)):
        if (
            sentence[x] == "a"
            or sentence[x] == "e"
            or sentence[x] == "i"
            or sentence[x] == "o"
            or sentence[x] == "u"
        ):
            count += 1
    return count


# def get_count(sentence):
#     return sum(1 for x in sentence if x in "aeiouAEIOU")


def get_count(sentence):
    return sum(x in "aeiou" for x in sentence)


print(get_count("aedpkgh"))


def disemvowel(string_):
    li = []
    for x in range(len(string_)):
        if (
            string_[x] == "a"
            or string_[x] == "e"
            or string_[x] == "i"
            or string_[x] == "o"
            or string_[x] == "u"
            or string_[x] == "A"
            or string_[x] == "E"
            or string_[x] == "I"
            or string_[x] == "O"
            or string_[x] == "U"
        ):
            string_ = string_.replace(string_[x], "")

            li.append(string_)
        else:
            li.append(string_[x])
    return li


print(disemvowel("This website is for losers LOL!"))
