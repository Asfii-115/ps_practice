# def count(s):
#     # The function code should be here

#     a = []
#     b = []
#     for x in s:
#         if x not in a:
#             a.append(x)
#     for x in a:
#         b.append(s.count(x))
#     return dict(zip(a,b))

from collections import Counter

def count(string):
    return Counter(string)

print(count('aba'))            

l1 = [1,2,3]
l2 = [1,2,3]

print(list(zip(l1,l2)))