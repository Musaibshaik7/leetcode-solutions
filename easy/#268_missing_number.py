nums=[0,1,2,3,4,6]

largest=len(nums)
for i in range(0,largest+1):
    if i not in nums:
        missing=i
        break
print(missing)