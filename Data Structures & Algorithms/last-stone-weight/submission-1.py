class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            elif stones[-1]< stones[-2]:
                k = stones.pop(-1)
                stones[-2] = stones[-2]-k
            elif stones[-2] < stones[-1]:
                k = stones.pop(-2)
                stones[-1] = stones[-1] - k
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0

        