nums1 = [1,2,3,0,0,0]
m = 3

left = m - 1
right = len(nums1) - 1

nums2 = [2,5,6]
n = 3
right2 = n - 1

while right2 >= 0:

    if left >= 0 and nums1[left] > nums2[right2]:
        nums1[right] = nums1[left]     
        left -= 1                        
    else:
        nums1[right] = nums2[right2]    
        right2 -= 1                     

    right -= 1                          
print(nums1)

