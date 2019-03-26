def factors(n):
    k = 1
    while k*k < n:
        if n%k == 0:
            yield k
            yield n//k
        k += 1
    if k*k == n:
            yield k

a = factors(100)
l = []
for i in a:
    l.append(i)
l.sort()
print(l)

# 不用额外空间能行吗？
