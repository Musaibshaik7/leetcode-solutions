nums=[1,2,3,4]
nums=[1,2,3,4]
for el in range(0,len(nums)):
   if(el==0):
       continue
   nums[el]+=nums[el-1]
print(nums)   
   nums[el]+=nums[el-1]
print(nums)