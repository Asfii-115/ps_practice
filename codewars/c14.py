def shuffler(x):
    return " ".join(x.split()[::-1])


print(shuffler("asfi ahmed"))


def combat(h, d):
    return max(0, h - d)
