def even_list(l):
  x=[]
  for a in l:
    if a%2==0:
      x.append(a)
  return x

print(even_list([1,2,3,4]))      