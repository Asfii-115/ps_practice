def max_two(x,y):
  if x>y:
    return x
  return y

def max_three(x,y,z):
  return max_two(x,max_two(y,z))  

print(max_three(3,6,-8))    
      
