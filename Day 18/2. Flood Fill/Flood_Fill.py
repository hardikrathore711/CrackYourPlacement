class Solution:
    def traverse(self,r,c,org,color,image):
        if r<0 or c<0 or r==len(image) or c==len(image[0]) or image[r][c]!=org or image[r][c]==color:
            return
        image[r][c] = color
        self.traverse(r-1,c,org,color,image)
        self.traverse(r,c-1,org,color,image)
        self.traverse(r+1,c,org,color,image)
        self.traverse(r,c+1,org,color,image)

    def floodFill(self, image, sr, sc, color):
        org = image[sr][sc]
        self.traverse(sr,sc,org,color,image)
        return image
        