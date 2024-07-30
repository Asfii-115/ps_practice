str1 = input()
str2 = input()
l = []
for x in str1:
    l.append(x)

i = 0
count = 0
for x in str2:
    if x == l[i]:
        count += 1
        i += 1
    else:
        i += 1
print(count)


def count_matching_characters(str1, str2):
    # Convert strings to sets to get unique characters
    set1 = set(str1)
    set2 = set(str2)

    # Find the intersection of both sets
    common_chars = set1.intersection(set2)

    # Count the number of common characters
    return len(common_chars), common_chars


# Test cases
str1 = "abcdef"
str2 = "defghia"
output, characters = count_matching_characters(str1, str2)
print(f'Input: str1 = "{str1}", str2 = "{str2}"')
print(f'Output: {output} (i.e. matching characters :- {", ".join(characters)})')

str1 = "aabcddekll12@"
str2 = "bb2211@55k"
output, characters = count_matching_characters(str1, str2)
print(f'Input: str1 = "{str1}", str2 = "{str2}"')
print(f'Output: {output} (i.e. matching characters :- {", ".join(characters)})')
