string = input()
mid = len(string) // 2
new = string[mid:].upper()
print(string[:mid] + new)
