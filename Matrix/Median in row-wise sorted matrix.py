class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                t = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = t
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
