def meeting(s):
    s = s.split(";")
    y = sorted(s, key=lambda x: x.split(":")[1])
    z = tuple(map(lambda x: x.upper(), y))
    li = []
    for i in z:
        o = i.replace(":", ", ")
        li.append(o)
    return z


print(
    meeting(
        "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
    )
)
p = "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"

# Step 1: Split the input string into a list of names
names = p.split(";")

# Step 2: Sort the list of names by last name first, and by first name second
sorted_names = sorted(
    names, key=lambda name: (name.split(":")[1].upper(), name.split(":")[0].upper())
)

# Step 3: Format each name in the form (LASTNAME, FIRSTNAME)
formatted_names = [
    f"({last.upper()}, {first.upper()})"
    for first, last in (name.split(":") for name in sorted_names)
]

# Step 4: Join the formatted names into a single string
result = "".join(formatted_names)

print(result)
