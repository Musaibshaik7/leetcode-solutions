nums=[12,345,2,6,7896]
count=0
for el in nums:
    value=0
    temp=el
    while(temp!=0):
        value+=1
        temp//=10
        
    if(value%2==0):
        count+=1
print(count)  