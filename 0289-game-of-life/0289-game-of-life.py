class Solution:


    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def calculate(i,j):

            neighbours = 0
            status = 0

            if i-1>=0 and j-1>=0:
                status += board[i-1][j-1]
                neighbours+=1
            if i-1>=0:
                status += board[i-1][j]
                neighbours+=1
            if i-1>=0 and j+1<ncolumns:
                status += board[i-1][j+1]
                neighbours+=1
            if j+1<ncolumns:
                status += board[i][j+1]
                neighbours+=1
            if i+1<nrows and j+1<ncolumns:
                status += board[i+1][j+1]
                neighbours+=1
            if i+1<nrows:
                status += board[i+1][j]
                neighbours+=1
            if i+1<nrows and j-1>=0:
                status += board[i+1][j-1]
                neighbours+=1
            if j-1>=0:
                status += board[i][j-1]
                neighbours+=1
            if board[i][j]==0 and status==3:
                return 1
            else:
                if status<2:
                    return 0
                if status==2 or status==3:
                    return board[i][j]
                if status>3:
                    return 0
        

        nrows = len(board)
        ncolumns = len(board[0])
        new_board = [[] for _ in range(nrows)]
        
        for i in range(nrows):
            for j in range(ncolumns):
                val = calculate(i,j)
                new_board[i].append(val)
            
        for i in range(nrows):
            for j in range(ncolumns):
                board[i][j] = new_board[i][j]
            


