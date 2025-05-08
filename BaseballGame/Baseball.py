from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == 'C':
                record.pop()
            elif op == 'D':
                record.append(2*record[-1])
            elif op == '+':
                record.append(record[-1] +record[-2])
            else:
                record.append(int(op))

        res = 0
        while record:
            res += record.pop()

        return res

if __name__ == '__main__':
    solution = Solution()
    ops = ["5", "2", "C", "D", "+"]
    print(solution.calPoints(ops))