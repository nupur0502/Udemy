def Factorial(nums):
    output = 1
    count = 0
    while(nums>=1):
        output = nums*output
        nums = nums-1
    while(output%10 == 0):
            count = count +1
            output = output/10
        
    return count
        
print(Factorial(3))
