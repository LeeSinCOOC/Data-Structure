def is_multiple(n,m):
    if m == 0:
        return '零除错误'
    if n < m:
        return '不能整除'
    if n%m :
        return False
    else:
        return True

a = is_multiple(20,10)
print(a)
        
