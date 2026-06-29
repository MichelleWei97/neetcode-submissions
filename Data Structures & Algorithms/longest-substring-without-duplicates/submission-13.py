class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ptr = 0
        ptr2 = 0
        lst = []
        max_sub = 0
        for i in range(len(s)):
            while s[i] in lst:
                ptr+= 1
                ptr2+= 1
                lst = lst[ptr2:]
                ptr2 = 0
            lst.append(s[i])
            max_sub = max(max_sub, i - ptr +1)
        return max_sub