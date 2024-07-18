class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        rowb=[False]*n
        columnb=[False]*m
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rowb[j]=True
                    columnb[i]=True
        for i in range(n):
            if rowb[i]==True:
                for j in range(m):
                    matrix[j][i]=0
        for i in range(m):
            if columnb[i]==True:
                for j in range(n):
                    matrix[i][j]=0
        return matrix
