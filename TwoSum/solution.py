def twoSum(num, target):
    map_num = {}
    for i in range(len(num)):
        diff = target - num[i]
        if num[i] in map_num:
            return [map_num[num[i]], i]
        else:
            map_num[diff]=i
            
    return []
print(twoSum([2, 7, 11, 15],9))