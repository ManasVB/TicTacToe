import numpy
import copy
import math
import random

X = "X"
O = "O"
EMPTY  = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x += 1
            if board[i][j] == O:
                o += 1
    if (x == 0 and o == 0) or (x == o):
        return 'X'
    elif x == (o+1):
        return 'O'

def actions(board):
    s = {3}
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                s.add((i, j))
    s.remove(3)
    return s

def result(board,action):
    s = actions(board)
    if not action in s:
        raise Exception("False")
    else:
        P = player(board)
        P = X if P == 'X' else O
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = P
        return new_board

def winner(board):
    t_arr = numpy.transpose(board)
    for j in range(3):
        if all(i == X for i in board[j]):
            return 'X'
        elif all(i == O for i in board[j]):
            return 'O'

    for j in range(3):
        if all(i == X for i in t_arr[j]):
            return 'X'
        elif all(i == O for i in t_arr[j]):
            return 'O'

    diag1 = [0,0,0]
    diag1[0] = board[0][0]
    diag1[1] = board[1][1]
    diag1[2] = board[2][2]
    if all(s == X for s in diag1):
        return 'X'
    elif all(s == O for s in diag1):
        return 'O'
    diag2 = [0,0,0]
    diag2[0] = board[0][2]
    diag2[1] = board[1][1]
    diag2[2] = board[2][0]
    if all(s == X for s in diag2):
        return 'X'
    elif all(s == O for s in diag2):
        return 'O'
    return None

def terminal(board):
    b = winner(board)
    if b == 'X' or b == 'O':
        return True
    for j in range(3):
        if not all(((s == X) or (s == O)) for s in board[j]):
            return False
    return True

def utility(board):
    b = winner(board)
    if b == 'X':
        return 1
    elif b == 'O':
        return -1
    elif b == None and terminal(board) == True:
        return 0

def minimax(board):
    if len(actions(board)) == 9:
        rand = random.choice(tuple(actions(board)))
        return rand
    else:
        if terminal(board) == True:
            return None
        else:
            P = player(board)
            if P == 'X':
               v = maxvalue(board)
               print(v)
               for s in actions(board):
                   new_board = result(board,s)
                   v1 = minvalue(new_board)
                   if v1 == v:
                       return s
            elif P == 'O':
               v = minvalue(board)
               print(v)
               for s in actions(board):
                   new_board = result(board,s)
                   v1 = maxvalue(new_board)
                   if v1 == v:
                       return s

def maxvalue(board):
    if terminal(board) == True:
        return utility(board)
    else:
        v = -math.inf
        for s in actions(board):
            new_board = result(board,s)
            v = max(v,minvalue(new_board))
        return v

def minvalue(board):
    if terminal(board) == True:
        return utility(board)
    else:
        v = math.inf
        for s in actions(board):
            new_board = result(board,s)
            v = min(v,maxvalue(new_board))
        return v
