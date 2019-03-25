from random import randrange

def my_chioce(data):
    a = randrange(1,10)
    s = int(str(a*a*77)[0])
    return data[s]

data = 'abcdefg'

a = my_chioce(data)
print(a)
    
    
    
