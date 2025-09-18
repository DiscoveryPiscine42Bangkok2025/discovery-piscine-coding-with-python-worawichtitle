"""rush/ex00/check.py"""
def findking(board):
    """find king position"""
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 'K':
                return (x, y)
    return None

def pawn_check(board, king_pos):
    """check pawn attack"""
    x_king, y_king = king_pos
    for x_pawn in range(len(board)):
        for y_pawn in range(len(board[x_pawn])):
            if board[x_pawn][y_pawn] == 'P':
                print(x_pawn, y_pawn)
                print(x_king, y_king)
                if (x_pawn - 1 == x_king) and (y_pawn - 1 == y_king or y_pawn + 1 == y_king):
                    return True
    return False

def rook_check(board, king_pos):
    """check rook attack"""
    x_king, y_king = king_pos
    # Check row
    for x_rook in range(len(board[y_king])):
        if board[x_king][x_rook] == 'R':
            return True
    # Check column
    for i in range(len(board)):
        if board[i][y_king] == 'R':
            return True
    return False

def check(board):
    """check if king safe"""
    listboard = board.split("\n")
    king = findking(listboard)
    print(listboard)
    print(king)
    print("King is in check by pawn", pawn_check(listboard, king))
    print("King is in check by rook", rook_check(listboard, king))

def main():
    """have board and call check"""
    board = """\
.R..
.K..
..P.
....\
"""
    check(board)

main()