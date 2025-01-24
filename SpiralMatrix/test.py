from SpiralMatrix import Solution

def main():
    solution = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    print(solution.spiralOrder(matrix))

if __name__ == '__main__':
    main()