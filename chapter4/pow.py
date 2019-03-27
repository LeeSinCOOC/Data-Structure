def power(x,n):
    if n == 0:
        return 1
    else:
        return power(x,n-1) * x

x = 10
n = 3
a = power(x,n)
print(a)
