nums=[1,2,3,4,5]
n=len(nums)
ans = []

for i in range(n):
    ans.append(nums[i])
    ans.append(nums[i + n])

print(ans)