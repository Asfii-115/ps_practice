def dig_pow(n, p):
    # your code
    c = 0
    for i,s in enumerate(str(n)):
        c+= pow(int(s),p+i)
    return c/n if c%n==0 else -1

print(dig_pow(46288,3))    
