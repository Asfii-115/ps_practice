#method 1

def uni_list(l):
  a= list(dict.fromkeys(l))
  return a

b=[1,2,2,3,3,4,5,5]
print(uni_list(b))  

#method 2

def unique_list(li):
  x=[]
  for a in li:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,2,3,3,4,5,5]))      