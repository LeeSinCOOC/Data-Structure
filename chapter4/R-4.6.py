def harmonic(n):
    if n == 1:
        return 1
    return harmonic(n-1) + 1/n

def harmonic_nor(n):
    sum_ = 0
    for i in range(1,n+1):
        sum_ += 1/i
    return sum_
        
a = harmonic(900)
print(a)

b = harmonic_nor(900)
print(b)
