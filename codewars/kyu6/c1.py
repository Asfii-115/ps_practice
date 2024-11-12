def unique_in_order(sequence):
    unique_list = [sequence[0]]
    for x in sequence:
        if x != unique_list[-1]:
            unique_list.append(x)
    return unique_list


print(unique_in_order("AAAABBBCCDAABBB"))
