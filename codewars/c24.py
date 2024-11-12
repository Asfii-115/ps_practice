def ordered_count(inp):
    ul = []
    cc = []
    for x in inp:
        if x not in ul:
            ul.append(x)
    for x in ul:
        c = inp.count(x)
        cc.append(c) 
    return list(zip(ul,cc))


from collections import Counter

def oc(input):
   return list(Counter(input).items())

print(oc('abracadabra')) 

# counter(your list).items() --- items so applies to all the values in the list