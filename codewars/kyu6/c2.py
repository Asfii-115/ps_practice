def is_pangram(st):
    s = st.lower()
    for x in "abcdefghijklmnopqrstuvwxyz":
        if x not in s:
            return False
        else:
            return True


print(is_pangram("The quick brown fox jumps over the lazy dog."))
