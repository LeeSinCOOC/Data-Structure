def reverse(s):
    return s[::-1]

def recursion(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + recursion(s[:-1])
s = 'abcdefg'
a = reverse(s)
b = recursion(s)
print(a)
print(b)
