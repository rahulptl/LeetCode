class Solution:


    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def calculate(i,j):

            neighbours = 0
            status = 0
            
            pairs = [
                (i-1,j-1),
                (i-1,j),
                (i-1,j+1),
                (i,j+1),
                (i+1,j+1),
                (i+1,j),
                (i+1,j-1),
                (i,j-1)
            ]
            for x,y in pairs:
                if 0<=x<nrows and 0<=y<ncolumns:
                    if board[x][y]==2:
                        val_to_add = 0
                    elif board[x][y]==-1:
                        val_to_add = 1
                    else:
                        val_to_add = board[x][y]

                    status+=val_to_add


            if board[i][j]==0:
                if status==3:
                    return 2
                else:
                    return 0
            else:
                if status<2:
                    return -1
                if status==2 or status==3:
                    return board[i][j]
                if status>3:
                    return -1
        

        nrows = len(board)
        ncolumns = len(board[0])
        new_board = [[] for _ in range(nrows)]
        
        for i in range(nrows):
            for j in range(ncolumns):
                val = calculate(i,j)
                board[i][j] = val
        
        for i in range(nrows):
            for j in range(ncolumns):
                if board[i][j]==-1:
                    board[i][j]=0
                if board[i][j]==2:
                    board[i][j]=1
