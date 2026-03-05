class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        #Record origninal zeros
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
                  # set row in zeros
        for r in zero_rows:
            for c in range(cols):
                matrix[r][c] = 0
        for c in zero_cols:
            for r in range(rows):
                matrix[r][c] = 0                    
        """
        Do not return anything, modify matrix in-place instead.
        """
        