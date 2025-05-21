class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        il = []
        jl = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    il.append(i)
                    jl.append(j)
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if i in il:
                    matrix[i][j] = 0
                if j in jl:
                    matrix[i][j] = 0
        return matrix