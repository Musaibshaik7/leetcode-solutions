arr=[0,0,1,1,1,2,2,3,3,4]
write=0
for read in range(1,len(arr)):
    if arr[read]!=arr[write]:
        temp=arr[read]
        arr[read]=arr[write+1]
        arr[write+1]=temp
        write+=1
        ''' i can also do
        arr[write+1]=arr[read]
        write+=1 
        because i dont need to preserve swapped elements
        '''
        
print(arr)
    