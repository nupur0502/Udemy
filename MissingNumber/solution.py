 def missingNumber(self, nums):
        i = 0
        while(i<len(nums)):
            if i in nums:
                i = i+1
            else:
                return i