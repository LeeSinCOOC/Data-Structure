def scale(data,factor):
    for i in range(len(data)):
        data[i] *= factor
    return data

data = [1,2,3]
factor = 2

a = scale(data,factor)
print(a)
