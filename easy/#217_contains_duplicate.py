arr1=[1,1,1,3,3,4,3,2,4,2] 
flag=False #optimized using set✅
seen=set()
for el in arr1:
   
    if el in seen:
        flag=True
        break
    seen.add(el)

#without optimization❌
# def containsDuplicate(self, nums: List[int]) -> bool:
#         duplicate = False
#         i = 0

#         while(i < len(nums)):
#             for x in range(i + 1, len(nums)):
#                 if(nums[i] == nums[x]):
#                     duplicate = True
#                     break

#             if duplicate:
#                 break

#             i += 1

#         if duplicate:
#             return True
#         else:
#             return False

    