class Solution:
    def setZeroes(self, matrix):
        r,c = len(matrix),len(matrix[0])
        row = set()
        column = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    row.add(i)
                    column.add(j)
        for i in row:
            for j in range(c):
                matrix[i][j] = 0
        
        for i in range(r):
            for j in column:
                matrix[i][j] = 0