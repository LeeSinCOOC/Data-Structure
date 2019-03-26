def fac():
    s = ''
    while True:
        a = input('---->')
        if a == '=':
            break
        s += a
    return eval(s) #eval() 函数用来执行一个字符串表达式，并返回表达式的值。

a = fac()
print(a)
    
