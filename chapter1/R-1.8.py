s = 'abcdefg'

def find(s,n):
    N = 0
    if n < 0:
        N = len(s) + n
        if N < 0:
            return '超出范围了'
    return N

a = find(s,-7)
print(a)
        
        
