height = [1,8,6,2,5,4,8,3,7]
left=0
right=len(height)-1
area=0
while left <right:
    width=right-left
    water_height=min(height[left],height[right])
    temp_area=width*water_height
    if(temp_area>area):
        area=temp_area
    if(height[left]<height[right]):
        left+=1
    else:
        right-=1

print(area)