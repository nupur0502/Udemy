def removezero(nums):

    i = 0
    length = len(nums)
    while(i<length):
       if nums[i] == 0:
           nums.append(nums[i])
           del nums[i]
           length = length - 1
       else:
            i = i+1
    return nums
print(removezero([0,0,1,0,5,5,0,7,1,0]))
