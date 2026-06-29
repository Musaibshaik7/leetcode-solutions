nums=[1,12,-5,-6,50,3]
k=4
max_sum=sum(nums[:k])
window_sum=max_sum
for el in range(k,len(nums)):
    window_sum=window_sum+nums[el]-nums[el-k]
    if window_sum>=max_sum:
        max_sum=window_sum
        store=nums[el-k+1:el+1]
print(f"{store}={max_sum}/{k}={max_sum/k}")
        
        

