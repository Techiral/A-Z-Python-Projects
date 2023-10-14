s = input("enter a word : ")
length = 0
mp = {}
ans = ""
windowStart = 0
for windowEnd in range(len(s)):
    mp[s[windowEnd]] = mp.get(s[windowEnd], 0) + 1
    while mp[s[windowEnd]] > 1:
        mp[s[windowStart]] -= 1
        windowStart += 1
    if(length < windowEnd-windowStart + 1):
        length = windowEnd-windowStart + 1
        ans = s[windowStart:windowEnd+1]
print("maximum length substring in a string :",ans)
