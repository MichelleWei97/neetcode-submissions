class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dict1 = {}
        lst = []
        lst_keys = []
        for i in points:
            distance = (math.sqrt(i[0]**2 + i[1]**2))
            if distance not in dict1:
                dict1[distance] = [i]
            else:
                dict1[distance].append(i)
        for i in dict1.keys():
            lst_keys.append(i)
        lst_keys.sort()
        res = []
        for key in lst_keys:
            for point in dict1[key]:
                if len(res) < k:
                    res.append(point)
        return res