#Enumerates all nodes and picks the best valued one
def minimax(node, depth, maximizing_y_or_n):
    if(depth == 0 or node.terminal_node()):
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

#Like minimax but it trims off useless nodes, making it possible to search deeper
def alphabeta(node, depth, alpha, beta, maximizing_y_or_n):
    if(depth == 0 or node.terminal_node()):
        return heuristic()

    if(myPlayer):
        bestValue = -infinity
        for move in possibleMoves:
            value = max(value, alphabeta(move_node, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if(beta <= alpha):
                break

        return value
    else:
        bestValue = infinity
        for move in possibleMoves:
            value = min(value, alphabeta(move_node, depth-1, alpha, beta, True))
            beta = min (beta, value)
            if(beta <= alpha):
                break
        return value

#The heuristic determines weights of moves, e.g what is valuable or not. 
def heuristic():
    return