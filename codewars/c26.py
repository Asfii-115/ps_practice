def words_to_marks(s):
    s = s.lower()
    c = 0
    for x in s:
        c+= ord(x)-96
    return c    

print(words_to_marks('ab'))