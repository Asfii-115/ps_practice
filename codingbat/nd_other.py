def end_other(a, b):
    a_lower = a.lower()
    b_lower = b.lower()
    length_a = len(a_lower)
    length_b = len(b_lower)
    if a_lower == b_lower[-length_a:]:
        return True
    elif b_lower == a_lower[-length_b:]:
        return True
    return False


print(end_other("Hiabc", "abc"))


def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return b.endswith(a) or a.endswith(b)
