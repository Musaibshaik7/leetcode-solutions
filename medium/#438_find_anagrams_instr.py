s="cbaebabacd"
p="abc"

if len(p)>len(s):
    print([])
else:

    result=[]

    p_count={}
    window_count={}

    for ch in p:
        p_count[ch]=p_count.get(ch,0)+1

    k=len(p)

    for i in range(k):
        window_count[s[i]]=window_count.get(s[i],0)+1

    if window_count==p_count:
        result.append(0)

    for right in range(k,len(s)):

        leaving=s[right-k]

        window_count[leaving]-=1

        if window_count[leaving]==0:
            del window_count[leaving]

        entering=s[right]

        window_count[entering]=window_count.get(entering,0)+1

        if window_count==p_count:
            result.append(right-k+1)

    print(result)