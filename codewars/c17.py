# def duplicate_count(text):
#     text = text.lower()  # Convert text to lowercase to handle case insensitivity
#     seen = set()  # To track already counted characters
#     duplicates = set()  # To track duplicates found

#     for char in text:
#         if char in seen:
#             duplicates.add(char)
#         else:
#             seen.add(char)

#     return len(duplicates)


# # Test the function
# print(duplicate_count("aabbcde"))  # Expected output: 2


def dupli(word):
    return sorted(word.split())


print(dupli("4of Fo1r pe6ople g3ood th5e the2"))


def alphabet_position(text):
    li = []
    s = []
    text = text.lower()
    for x in range(len(text)):
        if text[x].isalpha():
            li.append(text[x])
    for x in li:
        s.append(ord(x) - 96)

    return text


print(alphabet_position("The sunset sets at twelve o' clock."))


def ap(text):
    return " ".join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


print(ap("The sunset sets at twelve o' clock."))
