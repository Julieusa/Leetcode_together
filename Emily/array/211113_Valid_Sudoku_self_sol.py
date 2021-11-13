class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row=sorted(board[i])
            for j in range(len(row)-1):
                if row[j]==row[j+1] and row[j]!='.':
                    return False
        
        for n in range(9):
            find_col=[]  
            for m in range(9):
                find_col.append(board[m][n])
            col=sorted(find_col)
            for k in range(len(col)-1):
                if col[k]==col[k+1] and col[k]!='.':
                    return False
        a=b=0
        while a<=6:
            square=board[a][b:b+3]+board[a+1][b:b+3]+board[a+2][b:b+3]
            square=sorted(square)
            for num in range(len(square)-1):
                if square[num]==square[num+1] and square[num]!='.':
                    return False
            b+=3
            if b==9:
                a+=3
                b=0

        if a>6:
            return True
            
#Runtime: 88 ms, faster than 46.40% of Python online submissions for Valid Sudoku.
#Memory Usage: 13.6 MB, less than 18.90% of Python online submissions for Valid Sudoku.
#O(9*10)

def isValidSudoku(self, board):
    return (self.is_row_valid(board) and
            self.is_col_valid(board) and
            self.is_square_valid(board))

def is_row_valid(self, board):
    for row in board:
        if not self.is_unit_valid(row):
            return False
    return True

def is_col_valid(self, board):
    for col in zip(*board):
        if not self.is_unit_valid(col):
            return False
    return True
    
def is_square_valid(self, board):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not self.is_unit_valid(square):
                return False
    return True
    
def is_unit_valid(self, unit):
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit)
 #set(A) return the unique element in A
#zip(*board), *A is A transpose, zip is zip all list together (stack)
