nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
left=0
zero_count=0
max_length=0
for right in range(0,len(nums)):
    if nums[right]==0:
        zero_count+=1
        
    while zero_count>k:
        if nums[left]==0:
            zero_count-=1
            
        left+=1
    window_length=right-left+1
    if window_length>max_length:
        max_length=window_length
print(max_length)

       
       
        
        
        
    
    
    