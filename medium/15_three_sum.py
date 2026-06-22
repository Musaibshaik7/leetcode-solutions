nums = [-1,0,1,2,-1,-4]
#[-4, -1, -1, 0, 1, 2]
nums.sort()
flag=False
el=0
result =set()
while el <len(nums):

    left=el+1
    right=len(nums)-1
    while left<right:
        if(nums[el]+nums[right]+nums[left]==0):
           result.add((nums[el],nums[left],nums[right]))
           left+=1
           right-=1
            
        elif(0<nums[right]+nums[left]+nums[el]):
            right-=1
        else:
            left+=1
        
    el+=1
found=[list(x) for x in result]
print(found)


    


    