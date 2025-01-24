from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        #Transpose
        for row in range(rows):
            for col in range(cols):
                if row < col:
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        #Horizontal Reflection
        for row in range(rows):
            for col in range(cols//2):
                matrix[row][col], matrix[row][cols - col - 1] = matrix[row][cols - col - 1], matrix[row][col]
