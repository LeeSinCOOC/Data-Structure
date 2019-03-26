from random import randint

def my_shuffle(data):
    l = []
    while True:
        if len(data) == 0:
            break
        s = randint(0,len(data)-1) #注意两端点值也能取到
        a = data.pop(s)
        l.append(a)
    return l

data = [1,2,3,4,5,6]
a = my_shuffle(data)
print(a)
        
        
