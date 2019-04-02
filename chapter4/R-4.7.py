def string(s):
    ss = ''
    for i in s:
        if i.isdigit():
            ss += i
    return ss           

s = '12345..4'
a = string(s)
print(a)

# 递归
