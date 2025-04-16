from typing import List
import heapq

#Iterative solution
class Solution1:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [""] * len(score)
        flag = 1
        score_with_index = [(val, idx) for idx, val in enumerate(score)]
        score_with_index.sort(reverse=True)

        for val, idx in score_with_index:
            if flag == 1:
                res[idx] = "Gold Medal"
                flag += 1
            elif flag == 2:
                res[idx] = "Silver Medal"
                flag += 1
            elif flag == 3:
                res[idx] = "Bronze Medal"
                flag += 1
            else:
                res[idx] = str(flag)
                flag += 1

        return res

#Max-heap solution
class Solution2:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [""] * len(score)
        score = [(-val, idx) for idx, val in enumerate(score)]
        heapq.heapify(score)
        rank = 1

        while len(score) > 0:
            cur_val, cur_idx = heapq.heappop(score)
            if rank == 1:
                res[cur_idx] = "Gold Medal"
                rank += 1
            elif rank == 2:
                res[cur_idx] = "Silver Medal"
                rank += 1
            elif rank == 3:
                res[cur_idx] = "Bronze Medal"
                rank += 1
            else:
                res[cur_idx] = str(rank)
                rank += 1

        return res