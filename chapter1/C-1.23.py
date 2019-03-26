def out_range(list_,x):
    try:
        return list_[x]
    except:
        return '越界了'

list_ = [1,2,3,4]
a = out_range(list_,3)
print(a)
