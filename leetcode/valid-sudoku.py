class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        coll = defaultdict(set)
        row = defaultdict(set)
        cont = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row[i] or board[i][j] in coll[j] or board[i][j] in cont[i //3 , j // 3]:
                    return False
                coll[j].add(board[i][j])
                row[i].add(board[i][j])
                cont[i//3,j//3].add(board[i][j])
        return True