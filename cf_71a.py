x=int(input())
for i in range(x):
  y=input()
  if len(y)>10:
    print(y[0] + str(len(y)-2) +y[len(y)-1]) 
  else:
    print(y)    