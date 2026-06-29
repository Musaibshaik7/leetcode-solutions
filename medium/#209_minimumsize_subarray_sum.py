nums=[2,3,1,2,4,3]
target=7

left=0
window_sum=0
min_length=float("inf")

for right in range(len(nums)):

    window_sum+=nums[right]

    while window_sum>=target:

        window_length=right-left+1

        if window_length<min_length:
            min_length=window_length

        window_sum-=nums[left]
        left+=1

if min_length==float("inf"):
    print(0)
else:
    print(min_length)