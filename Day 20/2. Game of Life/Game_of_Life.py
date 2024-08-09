class Solution:
    def gameOfLife(self, matrix: List[List[int]]) -> None:
        new = []
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(matrix[i][j])
            new.append(temp)
        for i in range(m):
            for j in range(n):
                c0,c1 = 0,0
                for k in range(-1,2):
                    for l in range(-1,2):
                        if k==0 and l==0:
                            continue
                        if (i+k)<0 or (j+l)<0 or (i+k)==m or (j+l)==n:
                            continue
                        if matrix[i+k][j+l] == 1:
                            c1+=1
                        else:
                            c0+=1
                if matrix[i][j] == 1:
                    if c1<2 or c1>3:
                        new[i][j] = 0
                else:
                    if c1==3:
                        new[i][j] = 1
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = new[i][j]
        