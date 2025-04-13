from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        root1 = p
        root2 = q
        q1 = deque([root1])
        q2 = deque([root2])

        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()

            if n1.val != n2.val:
                return False

            if n1.left and n2.left:
                q1.append(n1.left)
                q2.append(n2.left)
            elif n1.left or n2.left:
                return False

            if n1.right and n2.right:
                q1.append(n1.right)
                q2.append(n2.right)
            elif n1.right or n2.right:
                return False

        return not q1 and not q2
