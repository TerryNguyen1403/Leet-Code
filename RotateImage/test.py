from RotateImage import Solution

def main():
    solution = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

    solution.rotate(matrix)

    print(matrix)

if __name__ == '__main__':
    main()