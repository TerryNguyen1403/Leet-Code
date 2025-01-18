from MergedIntervals import Solution

def main():
    solution = Solution()
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[1,4],[1,5]]

    print(solution.merge(intervals))

if __name__ == '__main__':
    main()