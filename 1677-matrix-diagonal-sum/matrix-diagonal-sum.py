class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for r in range(n):
            for c in range(n):
                if r==c:
                    total += mat[r][c]
                elif r+c == n-1:
                    total += mat[r][c]
        return total                
        
        
       


        