# def abbrev_name(name):
#     first, last = name.upper().split(' ')
#     return first[0]+'.'+last[0]




def abbrev_name(name):
    return '.'.join(x[0] for x in name.split()).upper()
    
print(abbrev_name("Sam harris"))    