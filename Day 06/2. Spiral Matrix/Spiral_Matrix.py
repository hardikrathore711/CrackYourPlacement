class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        wup,wd,wl,wr = -1,m,-1,n
        dr = 0
        i,j = 0,0
        ans =[]
        sahi = True
        while sahi:
            sahi = False
            if dr==0:
                while j<wr:
                    sahi = True
                    ans.append(matrix[i][j])
                    j+=1
                j-=1
                i+=1
                wup+=1
                dr = (dr+1)%4
            elif dr==1:
                while i<wd:
                    sahi = True
                    ans.append(matrix[i][j])
                    i+=1
                i-=1
                j-=1
                wr-=1
                dr = (dr+1)%4
            elif dr==2:
                while j>wl:
                    sahi = True
                    ans.append(matrix[i][j])
                    j-=1
                j+=1
                i-=1
                wd-=1
                dr = (dr+1)%4
            else:
                while i>wup:
                    sahi = True
                    ans.append(matrix[i][j])
                    i-=1
                i+=1
                j+=1
                wl+=1
                dr = (dr+1)%4
        return ans
