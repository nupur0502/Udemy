 def removeDuplicates(nums):
    index = 1;
    length = len(nums)
    while (index < length):
        if (nums[index] == nums[index - 1]):
            del nums[index]
            index = index - 1
            length = length - 1

        index = index + 1

    return len(nums)
print(removeDuplicates([1,1,3,4]))