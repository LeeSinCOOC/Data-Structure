def backstr(s):
    return True if s == s[::-1] else False

def recursion(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return recursion(s[1:-1])
    else:
        return False
     
        
s = 'abcdcba'
a = backstr(s)
b = recursion(s)
print(a)
print(b)
