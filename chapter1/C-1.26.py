def arithmetic():
    a = int(input('a:'))
    b = int(input('b:'))
    c = int(input('c:'))

    if a + b == c or a == b - c or a*b == c:
        return True
    return False

# 算术逻辑的本质是？
# 还有许多情况需要考虑

a = arithmetic()
print(a)
