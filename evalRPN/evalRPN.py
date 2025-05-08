from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums_stack = []

        for c in tokens:
            if c != '+' and c != '-' and c != '*' and c != '/':
                nums_stack.append(int(c))
            elif c == '+':
                second_num = nums_stack.pop()
                first_num = nums_stack.pop()
                nums_stack.append(first_num + second_num)
            elif c == '-':
                second_num = nums_stack.pop()
                first_num = nums_stack.pop()
                nums_stack.append(first_num - second_num)
            elif c == '*':
                second_num = nums_stack.pop()
                first_num = nums_stack.pop()
                nums_stack.append(first_num * second_num)
            elif c == '/':
                second_num = nums_stack.pop()
                first_num = nums_stack.pop()
                nums_stack.append(first_num // second_num)

        return nums_stack.pop()

if __name__ == '__main__':
    solution = Solution()
    tokens= ["4","13","5","/","+"]

    print(solution.evalRPN(tokens))