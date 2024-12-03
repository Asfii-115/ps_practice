def char_count(s):
    count = {}
    for x in s:
        if x not in count:
            count[x] = 0
        count[x]+=1
    return count        

def anagram(s1,s2):
    return char_count(s1)==char_count(s2)

print(anagram('restful', 'fluster'))

def most_freq_char(s):
    count = {}
    for x in s:
        if x not in count:
            count[x] = 0
        count[x]+=1

    f_char = None
    for x in count:
        if f_char is None or count[x]>count[f_char]:
            f_char = x
    return f_char

print(most_freq_char('bookeeper'))    

def pair_sum(nums,target):
    prev_numbers = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in prev_numbers:
            return(prev_numbers[complement],index)
        prev_numbers[num] = index

print(pair_sum([3, 2, 5, 4, 1], 8)) 

def uncompress(s):
    i = 0
    j = 0
    res = []
    numbers = '0123456789'
    while j < len(s):
        if s[j] in numbers:
            j+=1
        else:
            num = int(s[i:j]) 
            res.append(num*s[j])
            j+=1
            i = j
            
    return ''.join(res)    
print(uncompress('2c3a1t')) 

def compress(s):
    s+='!'
    i = 0
    j = 0
    res = []
    while j < len(s):
        if s[j]==s[i]:
            j+=1
        else:
            val = j - i
            if val==1:
                res.append(s[i])
            else:
                res.append(str(val))
                res.append(s[i])
            i = j    
    return ''.join(res)
print(compress('ccaaatss'))                

