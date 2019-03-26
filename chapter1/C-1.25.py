def duplicate(s):
    S = ''
    for i in s:
        if ord(i) in list(range(97,97+26)) or ord(i) in \
           list(range(65,90)) or i == ' ':
            S += i
    return S

s = "let's try,Mike."
a = duplicate(s)
print(a)
