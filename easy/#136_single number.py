nums = [4, 1, 2, 1, 2]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    if freq[key] == 1:
        print(key)
        break