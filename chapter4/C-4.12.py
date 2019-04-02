def mn(m,n):
    if n == 1:
        return m
    return mn(m,n-1) + m

a = mn(10,5)
print(a)
