arr=[3,2,3]
freq={}
for el in arr:
    count=0
    if el not in freq:
        for el2 in range(0,len(arr)):
            if(el==arr[el2]):
                count+=1
            freq[el]=count
    
        if(freq[el]>len(arr)//2):
            print(el)
            break