def searchInsert(nums, target):
    new_array = []
    index = 0
    if target in nums:
        index = nums.index(target)
    elif (nums[len(nums)-1] < target):
        index = len(nums)
    else:
        for i in range(len(nums)):
            if(nums[i] < target):
                new_array.append(nums[i])
            else:
                new_array.append(target)
                new_array.append(nums[i])
        index = new_array.index(target)
    
    return index
                
print(searchInsert([1,3,5,6],0))