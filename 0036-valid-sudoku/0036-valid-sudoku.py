from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        bsquare = [[] for _ in range(9)]

        valid = True
        print(f"{rows=} {columns=}")

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    square1, square2 = ((i)//3), ((j)//3)
                    if board[i][j] in rows[i]:
                        return False
                    if board[i][j] in columns[j]:
                        return False
                    if board[i][j] in bsquare[square1*3+square2]:
                        return False
                    rows[i].append(board[i][j])
                    columns[j].append(board[i][j])
                    bsquare[square1*3+square2].append(board[i][j])
        # for  i in range(0,9):
        #     if len(set(rows[i])) < len(rows[i]):
        #         return False
        #     if len(set(columns[i]))<len(columns[i]):
        #         return False
        #     if len(set(bsquare[i])) < len(bsquare[i]):
        #         return False
        #print(f"{rows=} {columns=} {bsquare=}")
        return True
