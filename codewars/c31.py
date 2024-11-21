from collections import Counter


def fav_singer(n, singers):
    singer_count = Counter(singers)

    max_v = max(singer_count.values())

    fav = sum(1 for x in singer_count.values() if max_v == x)

    return fav


print(fav_singer(5, [1, 2, 2, 3, 3]))
