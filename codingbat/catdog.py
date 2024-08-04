def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for x in range(len(str) - 2):
        if str[x : x + 3] == "cat":
            count_cat += 1
        elif str[x : x + 3] == "dog":
            count_dog += 1
    if count_cat == count_dog:
        return True
    return False


print(cat_dog("catcat"))
