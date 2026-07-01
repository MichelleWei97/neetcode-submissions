class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        lst = []
        values = [0]*26
        for i in strs:
            for k in i:
                values[ord(k)-ord("a")] += 1
            res[tuple(values)].append(i)
            values = [0]*26
        return list(res.values())
            
        