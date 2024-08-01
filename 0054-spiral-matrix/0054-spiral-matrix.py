class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top =0 
        right = len(matrix[0])-1
        left = 0 
        bottom = len(matrix)-1
        traversed = []
        while top<=bottom and left<=right:
            print(top, bottom, left, right)
            for j in range(left, right+1):
                traversed.append(matrix[top][j])
            top+=1
            print(top, bottom, left, right)

            for j in range(top, bottom+1):
                traversed.append(matrix[j][right])

            right-=1
            if top<=bottom:
                for j in range(right, left-1, -1):
                    traversed.append(matrix[bottom][j])
                bottom-=1

            if left<=right:
                for j in range(bottom, top-1,-1):
                    traversed.append(matrix[j][left])
                
                left+=1


        return traversed
