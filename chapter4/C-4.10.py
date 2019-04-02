def div2c(n):
    count = 0
    while n >= 2:
        n //= 2
        count += 1
    return count

def div2r(n,c):
    if n <= 1:
        return 0,c
    return div2r(n//2,c+1)

a = div2c(32)
print(a)

b = div2r(32,0)
print(b)
    
