def binary_search(data,target,low,high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True,mid
        elif target < data[mid]:
            return binary_search(data,target,low,mid-1) #注意这里的边界，虽然mid不妨碍
        else:
            return binary_search(data,target,mid+1,high)
        
data = list(range(10,100,2))
a = binary_search(data,20,0,len(data))
print(a)
        
