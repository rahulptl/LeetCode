class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = set()
        columns = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows.add(i)
                    columns.add(j)

        for i in rows:
            matrix[i] = [0]*len(matrix[i])
        
        for i in columns:
            for j in range(len(matrix)):
                matrix[j][i] = 0
            
        print(matrix)
            