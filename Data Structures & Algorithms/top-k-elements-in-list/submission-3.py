class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        return_lst = []
        dict_to_lst = []
        ptr = 0
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            elif i not in dict1:
                dict1[i] = 1
        for i in dict1:
            dict_to_lst.append([dict1[i],i])
        dict_to_lst.sort()
        for i in range(1,k+1):
            return_lst.append(dict_to_lst[-i][1])
        return return_lst

        