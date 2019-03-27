def power(x,n):
    if n == 0:
        return 1
    mid = n // 2
    partial = power(x,mid)
    res = partial * partial
    if n % 2 == 1:
        res = res * x
    return res
def power_bad(x,n):
    if n == 0:
        return 1
    res = power_bad(x,n-1) * x
    return res

a = power(3,4)
print(a)

b = power(2,5)
print(b)
