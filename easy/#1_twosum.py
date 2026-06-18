nums = [1,2,5,7,10]
target = 3

i = 0
flag = 0

while(i < len(nums)):
    for el in range(i+1, len(nums)):
        if(nums[i] + nums[el] == target):
            found = [i, el]
            flag = 1
            break

    if flag:
        break

    i += 1

if flag:
    print(found)
else:
    print("not found")