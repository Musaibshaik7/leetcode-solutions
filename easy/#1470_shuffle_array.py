nums = [2,5,1,3,4,7]
n=3
nums2=[]
for i in range(n):
    nums2.append(nums[i])
    nums2.append(nums[n+i])
    
print(nums2)