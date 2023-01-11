def minimax(depth, index, maximizingPlayer,values, alpha, beta):
    if depth == 3:
        return values[index]
    
    
    if maximizingPlayer:
        optimum = MIN
    
        for i in range(0, 2):
            val = minimax(depth + 1, index * 2 + i,
            False, values, alpha, beta)
            optimum = max(optimum, val)
            alpha = max(alpha, optimum)
            if beta <= alpha:
                break
        return optimum
    
    else:
        optimum = MAX
        for i in range(0, 2):
            val = minimax(depth + 1, index * 2 + i,
            True, values, alpha, beta)
            optimum = min(optimum, val)
            beta = min(beta, optimum)
            if beta <= alpha:
                break
            
        return optimum
# Driver Code
if _name_ == "_main_":
    values = [2,3,5,9,0,1,7,5]
    print("The value is :", minimax(0, 0, True, values, MIN, MAX))
