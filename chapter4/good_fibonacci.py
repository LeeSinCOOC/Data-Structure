def good_fibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a,b) = good_fibonacci(n-1)
        return (a+b,a)

a = good_fibonacci(2)
print(a)

# 理解思想
