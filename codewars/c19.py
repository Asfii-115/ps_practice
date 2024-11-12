def add_binary(a,b):
    x = bin(a+b)
    return x.replace('0b','') #better to just show without 0b like [2:]
print(add_binary(2,3))

def nb_yeara(p0, percent, aug, p):
    # your code
    p_new = p0
    i = 0
    per = percent/100
    while p_new<p:
        i+=1
        p_new = p_new + int(p_new*per) + aug
    return i

print(nb_yeara(1000, 2, 50, 1200))

def nb_year(p0, percent, aug, p):
    # p0 - начальное население, percent - процент добавления, aug - пребывающие каждый год, p - что нужно превзойти
    per = percent/100
    pn = p0
    i = 0
    while pn < p:
        i = i + 1
        pn = int(pn + pn * per + aug)
        
    return i
print(nb_yeara(1000, 2, 50, 1200))


def is_triangle(a, b, c):
    s = a+b+c
    m = max(a,b,c)
    t = s-m
    return False if t<=m else True #better: just sort and return a+b>c

print(is_triangle(1,2,3))


def row(n):
    return n**3

print(row(2))

def gimme(input_array):
    #a,b,c = sorted(input_array)
    return input_array.index(sorted(input_array)[1])
print(gimme([2,3,1]))