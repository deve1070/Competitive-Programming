class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])
        matrix_t=[[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                matrix_t[j][i]=matrix[i][j]
        
        return matrix_t

