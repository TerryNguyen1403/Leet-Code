from InorderTraversal import TreeNode as Node
from InorderTraversal import Solution

if __name__ == '__main__':
    node2 = Node(2)
    node3 = Node(3)
    root = Node(1)

    root.right = node2
    node2.left = node3

    solution = Solution()
    print(solution.inorderTraversal(root))