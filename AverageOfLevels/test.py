from AverageOfLevels import TreeNode as Node
from AverageOfLevels import Solution

if __name__ == '__main__':
    root = Node(3)
    node2 = Node(9)
    node3 = Node(20)
    node4 = Node(15)
    node5 = Node(7)


    root.left = node2
    root.right = node3
    node3.left = node4
    node3.right = node5

    solution = Solution()
    print(solution.averageOfLevels(root))
