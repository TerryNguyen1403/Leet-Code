from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []

        while q:
            current_sum = 0
            current_size = len(q)
            i = 0

            while i < current_size:
                current_node = q.popleft()
                current_sum += current_node.val

                if current_node.left:
                    q.append(current_node.left)

                if current_node.right:
                    q.append(current_node.right)

                i += 1

            res.append(current_sum/current_size)

        return res
