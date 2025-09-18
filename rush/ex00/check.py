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
                if (x_pawn - 1 == x_king) and (y_pawn - 1 == y_king or y_pawn + 1 == y_king):
                    return True
    return False

def rook_check(board, king_pos, character='R'):
    """check rook attack"""
    x_king, y_king = king_pos
    attack = False
    king = False
    # หาแนวนอน
    for x_rook in range(len(board)):
        if board[x_king][x_rook] == 'K':
            king = True
        elif board[x_king][x_rook] == character:
            attack = True
        elif board[x_king][x_rook] != '.':
            attack = False
            king = False
        if attack and king:
            return True

    attack = False
    king = False
    # หาแนวตั้ง
    for y_rook in range(len(board)):
        if board[y_rook][y_king] == 'K':
            king = True
        elif board[y_rook][y_king] == character:
            attack = True
        elif board[y_rook][y_king] != '.':
            attack = False
            king = False
        if attack and king:
            return True
    return False

def bishop_check(board, king_pos, character='B'):
    """check bishop attack"""
    x_king, y_king = king_pos
    # ++ ขวาบน
    i = 1 
    for x in range(x_king + 1 , len(board)+1):
        if y_king + i >= len(board) or x >= len(board):
            break
        if board[x][y_king+i] == character:
            return True
        elif board[x][y_king+i] != '.':
            break
        i += 1
    # +- ขวาล่าง
    i = 1
    for x in range(x_king + 1, len(board)+1):
        if y_king - i < 0 or x >= len(board):
            break
        if board[x][y_king-i] == character:
            return True
        elif board[x][y_king-i] != '.':
            break
        i += 1
    # -+ ซ้ายบน
    i = 1
    for x in range(x_king - 1, -1, -1):
        if y_king + i >= len(board):
            break
        if board[x][y_king+i] == character:
            return True
        elif board[x][y_king+i] != '.':
            break
        i += 1
    # -- ซ้ายล่าง
    i = 1
    for x in range(x_king - 1, -1, -1):
        if y_king - i < 0:
            break
        if board[x][y_king-i] == character:
            return True
        elif board[x][y_king-i] != '.':
            break
        i += 1
    return False

def queen_check(board, king_pos):
    """check queen attack"""
    if rook_check(board, king_pos, 'Q') or bishop_check(board, king_pos, 'Q'):
        return True
    return False

def check(board):
    """check if king safe"""
    listboard = board.split("\n")
    king = findking(listboard)
    if pawn_check(listboard, king) or rook_check(listboard, king) or bishop_check(listboard, king) or queen_check(listboard, king):
        print("Success")
    else:
        print("Fail")
    # print(listboard)
    # print(king)
    # print("King is in check by pawn", pawn_check(listboard, king))
    # print("King is in check by rook", rook_check(listboard, king))
    # print("King is in check by bishop", bishop_check(listboard, king))
    # print("King is in check by queen", queen_check(listboard, king))