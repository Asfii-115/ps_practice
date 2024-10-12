def string_score(s):
    count = 0
    for x in range(1, len(s)):
        count += abs(ord(s[x]) - ord(s[x - 1]))
    return count


print(string_score("hello"))
