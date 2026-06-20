s= "A man, a plan, a canal: Panama"
s=s.lower()
ls=[]
for ch in s:
    tr=ch.isalnum()
    if(tr):
        ls.append(ch)
left=0
right=len(ls)-1
while(left<right):
    if(ls[left]!=ls[right]):
        print("not palindrome")
        break
    left+=1
    right-=1
else:
    print("palindrome")
