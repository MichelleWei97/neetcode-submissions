class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr = 0
        best = 0
        lst = []
        for i in range(len(s)):
            while s[i] in lst:
                lst.pop(0)
                ptr += 1
            if s[i] not in lst:
                lst.append(s[i])
            best = max(i - ptr + 1, best)
        return best
            