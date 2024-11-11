def is_anagram(test,original):
    return sorted(test.lower())==sorted(original.lower())

print(is_anagram('Buckethead',"DeathCubeK"))

def reverse_letter(s):
    y=''
    for x in s:
        if x.isalpha():
            y+=x

    return y[::-1]

print(reverse_letter('a89sfi'))

def check_exam(arr1,arr2):
    res = 0
    for x in range(len(arr1)):
        if arr1[x]==arr2[x]:
            res+=4
        if arr1[x]!=arr2[x]:
            res-=1
    r = res + arr2.count('')       
    return 0 if r<=0 else r

print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]))     

x = ['','a','b']
print(x.count(''))

def sum_digits(number):
    n = abs(number)
    return sum(int(x) for x in str(n))
print(sum_digits(-32))

def solve(s):
    uc = 0
    lc = 0
    for x in s:
        if x.islower():
            lc+=1
        else:
            uc+=1
    if lc>=uc:
        return s.lower()
    else:
        return s.upper()
    
    

def solved(s):
    upper = 0
    lower = 0
    
    for char in s:
        if char.islower():
            lower += 1
        else:
            upper += 1
            
    if upper == lower or lower > upper:
        return s.lower()
    else:
        return s.upper()
    
print(solve('CODe'))    

def max_multiple(divisor, bound):
    #your code here
    while bound>0:
        n = bound/divisor
        if n%1==0:
            return bound
        else:
            bound-=1
    return bound
print(max_multiple(37,200))        
