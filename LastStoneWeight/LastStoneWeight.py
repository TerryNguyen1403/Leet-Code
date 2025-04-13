import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = [-stones[i] for i in range(len(stones))]
        heapq.heapify(res)

        while len(res) > 1:
            first_stone = heapq.heappop(res)
            second_stone = heapq.heappop(res)

            if first_stone != second_stone:
                heapq.heappush(res, first_stone - second_stone)

        return - res[0] if res else 0