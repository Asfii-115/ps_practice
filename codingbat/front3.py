def front3(str):
    if len(str) < 3:
        return str * 3
    else:
        return str[:3] * 3


print(front3("as"))