# arr=[3,2,2,3,3,1,2,4]
# right=len(arr)-1
# left=0
# val=3
# while left<right:
#     if(arr[left]==val):
#         arr[left],arr[right]=arr[right],arr[left]
#         right-=1
#     if(arr[left]==val):
#         arr[left],arr[right]=arr[right],arr[left]
        
#     left+=1
# print(arr)
arr=[3,2,2,3,3,1,2,4]
write=0
val=3
for read in range(0,len(arr)):
    if(arr[read]!=val):
        arr[read],arr[write]=arr[write],arr[read]
        write+=1
print(arr)