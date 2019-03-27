def power_2(x,n):
    if n == 0:
        return 1
    else:
        partial = power_2(x,n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

x = 10
n = 3
a = power_2(x,n)
print(a)
