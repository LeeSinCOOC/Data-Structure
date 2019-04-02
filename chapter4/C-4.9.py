def minmax(s):
    n = len(s)
    min_ = s[0]
    max_ = s[0]
    for i in range(1,n):
        if s[i] < min_:
            min_ = s[i]
        if s[i] > max_:
            max_ = s[i]
    return min_,max_

s = [1,2,3,4,5]
a = minmax(s)
print(a)

# 递归求解？

def min_(s):
    if len(s) == 1:
        return s[0]
    if s[0] <= min_(s[1:]):
        return s[0]
    else:
        return min_(s[1:])
def max_(s):
    if len(s) == 1:
        return s[0]
    if s[0] >= min_(s[1:]):
        return s[0]
    else:
        return max_(s[1:])
def main(s):
    return min_(s),max_(s)

b = main(s)
print(b)
    
