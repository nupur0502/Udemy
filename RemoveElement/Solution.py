def RemoveElement(nums, val):
    index = 0
    length = len(nums)
    while(index<length):
        if nums[index]== val:
            del nums[index]
            index=index-1
            length = length -1
        index = index + 1
    return(len(nums))
print(RemoveElement([1,1,2,3,4,1,2,2,2],2))