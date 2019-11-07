#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Example:

#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
def removezero(nums):
    i = 0
    while(i<len(nums)):
        if nums[i] == 0:
           nums.append(nums[i])
           del nums[i]
        else:
            i = i+1
    return nums
print(removezero([0,0,0,3,0,12]))

