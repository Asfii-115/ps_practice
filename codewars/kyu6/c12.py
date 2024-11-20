def camel_case(s):
    s = s.split()
    return "".join(i.title() for i in s)


print(camel_case("hello case"))
