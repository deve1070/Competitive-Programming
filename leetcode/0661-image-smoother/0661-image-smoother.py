class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row,col=len(img),len(img[0])
        res=[[0]*col for _ in range(row)]
    
        for row_indx in range(row):
            for col_indx in range(col):
                res[row_indx][col_indx]=self.smoother(img,row_indx,col_indx)
        return res


    
    def smoother(self,img,x,y):
        row,col=len(img),len(img[0])
        off_sets=[(0,0),(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        sum_,count=0,0
        for off_set in off_sets:
            i,j=off_set
            nx,ny=i +x,y +j
            if 0<=nx<row and 0<=ny<col:
                sum_ +=img[nx][ny]
                count +=1
        return floor(sum_/count)
        


                