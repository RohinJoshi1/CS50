"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcounter = 0
    ocounter = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                xcounter += 1
            elif board[i][j] == O:
                ocounter += 1
    if xcounter > ocounter:
        return O
    else:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    posacts = set()
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                posacts.add((i, j))
    return posacts
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    output = copy.deepcopy(board)
    output[action[0]][action[1]] = player(board)
    return output
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
        # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
        # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if  winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) is X :
            return 1
        elif winner(board) is O :
            return -1
        else:
            return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    if current_player is X:
        v= -math.inf
        for action in actions(board):
            k = Min_value(result(board,action))
            if k>v:
                v=k;
                best_move = action
    else:
        v=math.inf
        for action in actions(board):
            k = Max_Value(result(board,action))
            if k<v:
                v=k
                best_move = action
    return best_move
    raise NotImplementedError
def Max_Value(board):
    if terminal(board):
        return utility(board)
    v= -math.inf
    for action in actions(board):
        v=max(v,Min_value(result(board,action)))
    return v
def Min_value(board):
    if terminal(board):
        return utility(board)
    v= math.inf
    for action in actions(board):
        v=min(v,Max_Value(result(board,action)))
    return v
