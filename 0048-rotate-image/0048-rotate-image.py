class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)

        for i in range(n):
            for j in range(n):

                if i>=j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):

            lp, rp = 0, n-1

            while lp<=rp:
                matrix[i][lp], matrix[i][rp] = matrix[i][rp], matrix[i][lp]
                lp+=1
                rp-=1
