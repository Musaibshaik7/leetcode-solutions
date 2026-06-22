# LeetCode 977 - Squares of a Sorted Array
nums = [-4, -1, 0, 3, 10]
left=0
right=len(nums)-1
el=len(nums)-1
result = [0] * len(nums)
while left<=right:
    if abs(nums[left]) > abs(nums[right]):
        result[el]=nums[left]**2
        el-=1
        left+=1
    else:
        result[el]=nums[right]**2
        el-=1
        right-=1
print(result)

        
    
           
           
        

