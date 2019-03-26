import os
'''
os.path.getsize(path)
os.path.isdir(path)
os.listdir(path)
os.path.join(path,filename)
'''
def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path): # 注意：没有path
            childpath = os.path.join(path,filename)
            total += disk_usage(childpath)
    return total

path = r'C:\Users\Administrator\Desktop\Data-Structure'
a = disk_usage(path)
print(a)
