def merge(word1, word2):
    result = ""
    i, j = 0, 0

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            result += word1[i]
            i += 1
        if j < len(word2):
            result += word2[j]
            j += 1

    return result


print(merge("abcd", "pqrqw"))
