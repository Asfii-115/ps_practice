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