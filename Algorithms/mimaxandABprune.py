def minimax(node, depth, maximizing_y_or_n):
    if(depth == 0):
        return heuristic()

    if(myPlayer):
        bestValue = -infinity
        for move in possibleMoves:
            value = minimax(move_node, depth-1, False)
            bestValue = max(bestValue, value)
        return bestValue

    else:
        bestValue = infinity
        for move in possibleMoves:
            value = minimax(move_node, depth-1, True)
            bestValue = min(bestValue, value)
        return bestValue


def alphabeta(node, depth, alpha, beta, maximizing_y_or_n):
    if(depth == 0 or self.game_ends(H,V)):
        return heuristic()

    if(myPlayer):
        bestValue = -infinity
        for move in possibleMoves:
            value = max(value, minimax(move_node, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if(beta <= alpha):
                break

        return value
    else:
        bestValue = infinity
        for move in possibleMoves:
            value = min(value, minimax(move_node, depth-1, alpha, beta, True))
            beta = min (beta, value)
            if(beta <= alpha):
                break
        return value

def heuristic():
    return