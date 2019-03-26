def scale(data,factor):
    for val in data:
        val *= factor
'''
return data 并没有改变值
'''

data = [1,2,3]
factor = 2

b = scale(data,factor)
print(b)
