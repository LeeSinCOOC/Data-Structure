from random import choice

def again():
    n = 0
    c = 0
    l = []
    s = 'I never spam my friends again.'
    while c < 8:
        a = choice([i for i in range(100)])
        if a not in l:
            l.append(a)
        c += 1
    while n < 100:
        l.sort()
        if n in l:
            print(s+choice([chr(i) for i in range(65,65+26)]))
        print(s)
        n += 1

a = again()

#还有很多更随机错误的方法未尝试
        
        
        
    
