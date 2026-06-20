arr=[0,1,2,0,0,8,7]
write=0
for read in range(0,len(arr)):
    if(arr[read]!=0):
        temp=arr[read]
        arr[read]=arr[write]
        arr[write]=temp
        write+=1
        

print(arr)
       


