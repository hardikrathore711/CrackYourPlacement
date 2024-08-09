class Solution:
    def __init__(self):
        self.ans = False
    def traverse(self,i,j,board,visited,word,ind):
        r,c = len(board),len(board[0])
        if len(word)==ind:
            self.ans = True
            return
        if self.ans:
            return 
        if i<0 or i==r or j<0 or j==c:
            return
        if visited[i][j]:
            return
        visited[i][j] = True
        if board[i][j]==word[ind]:
            self.traverse(i+1,j,board,visited,word,ind+1)
            self.traverse(i,j+1,board,visited,word,ind+1)
            self.traverse(i-1,j,board,visited,word,ind+1)
            self.traverse(i,j-1,board,visited,word,ind+1)
        visited[i][j] = False

    def exist(self, board, word):
        r,c = len(board),len(board[0])
        for i in range(r):
            for j in range(c):
                if board[i][j]==word[0]:
                    visited = [[False]*c for _ in range(r)]
                    self.traverse(i,j,board,visited,word,0)
        return self.ans