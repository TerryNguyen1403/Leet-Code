from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        my_stack = []
        cur_Node = root

        while cur_Node is not None or my_stack:
            while cur_Node is not None:
                my_stack.append(cur_Node)
                cur_Node = cur_Node.left

            cur_Node = my_stack.pop()
            res.append(cur_Node.val)
            cur_Node = cur_Node.right

        return res
