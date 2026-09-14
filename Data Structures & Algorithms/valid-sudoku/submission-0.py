class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        blocks = [set() for _ in range(9)]


        R, C = len(board), len(board[0])

        for i in range(R):
            for j in range(C):
                if (board[i][j] == "."):
                    continue
                
                else:
                    c = board[i][j]
                    b = (i // 3) * 3 + (j // 3)

                    if c in rows[i] or c in cols[j] or c in blocks[b]:
                        return False
                    
                    else:
                        rows[i].add(c)
                        cols[j].add(c)
                        blocks[b].add(c)
        
        return True