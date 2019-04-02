def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)
# 调用
a = hanoi(5, 'A', 'B', 'C')
print(a)

# 重点阅读
