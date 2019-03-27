def binary_search_iter(data,target):
    low = 0
    high = len(data)-1
    while low < high:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

data = [4,2,7,12,9,3]
target = 8
a = binary_search_iter(data,target)
print(a)
        
            
            
