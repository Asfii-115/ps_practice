# # def abbrev_name(name):
# #     first, last = name.upper().split(' ')
# #     return first[0]+'.'+last[0]




# def abbrev_name(name):
#     return '.'.join(x[0] for x in name.split()).upper()
    
# print(abbrev_name("Sam harris"))    

# def litres(time):
#     return int(time * 0.5)

# print(litres(6.7))    


# def lovefunc( flower1, flower2 ):
#     if flower1%2==0 and flower2%2 == 1:
#         return True
#     elif flower1 ==1 and flower2%2 ==0:
#         return True
#     return False

# print(lovefunc(2,2))    

# def lovefunc( flower1, flower2 ):
#     return (flower1+flower2)%2

# print(lovefunc(2,2))  

# def lovefunc(flower1, flower2):
#     return flower1 % 2 != flower2 % 2

def find_needle(haystack):
    return haystack.index('needle')

print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))    