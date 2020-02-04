from structs import node
import math, time, random

#Read Input
inputPlayer = int(input())
mancala1 = [int(input())]
mancala1_marbles = [int(i) for i in input().strip().split()]
mancala2 = [int(input())]
mancala2_marbles = [int(i) for i in input().strip().split()]
print(printNextMove(inputPlayer, mancala1, mancala1_marbles, mancala2, mancala2_marbles))

#Main function
def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):  
    state1 = mancala1_marbles[:]
    state2 = mancala2_marbles[:] 
    boardState = [state1, state2]
    mancalas = [mancala1, mancala2]
    treeRoot = structs.node(None, inputPlayer, boardState, mancalas)
    minimax = minimax_pruned()
    #TODO: Place Minimax here based off of initial board as root.
    #Send our player number to minimax as we are the original and we hardcode that we are maxer
    print("output")


'''
Main function. A/B Pruning is a feature of our minimax costing algorithm, so let's just roll the two into a single function.
'''
def minimax_pruned(treeRoot, cur_depth, alpha, beta, maxer, original): #Recursively explores the tree, rating nodes as they are reached. If we reach a place where the tree can be pruned, then we do NOT rate it.
    #Alpha and beta can be considered as a 'give me a better price or leave' metric. If the minimizer has a beta and the maximizer provides something higher than it, the minimizer will ignore the bargain - and visa versa.
        #if beta is less than alpha, then the opposing party being offered this deal will NEVER want the deal as the lowest acceptable bondary has been crossed.

    #If (current depth = 0 (maximum depth to be allowed)) or (current game board is in a finished state):
    if (cur_depth == 0):
    #   If the board is in a finished state, set heuristic value to 100% win rate for that node
        if (treeRoot.evalBoard()):
            if (treeRoot.player == original):
                return (1)
            else:
                return (0)

    #   Else run the heuristic function, returning that evaluation of the node.
        else:
            '''THIS IS WHERE WE KEEP THE HEURISTIC CALL'''                              
            heuristic = score_monteCarlo(treeRoot, 1, treeRoot.player)  #NOTE: might need to tweak time
            if (treeRoot.player == original):
                return (heuristic - 0.5)
            else:
                return (0.5 - heuristic)    #as 0.5 is the same winning chance for both players, we base our score off of how close/far we are from the 0.5 index
    # 
    #If the current player is the one seeking the maximum evaluation:
    if (maxer):
    #   current_max_eval = -infinity
        cur_max_eval = float("-inf")
    #   new_frontier = expand(current node)
        new_frontier = treeRoot.expand()
    #   for each of the children in the frontier:
        for child in new_frontier:
    #       evaluation = minimax_pruned(cur_child, current depth - 1, alpha, beta, (true/false depending on next player in this position))
            
            next_player = True if (child.player == original) else False
            p_eval = minimax_pruned(child, cur_depth - 1, alpha, beta, next_player, original)
    #       current_max_eval = max(current_max_eval, evaluation)
            cur_max_eval = max(cur_max_eval, p_eval)
    #       alpha = max(alpha, evaluation)
            alpha = max(alpha, p_eval)
    #       if beta <= alpha: <-- which is to say, if the MINIMIZER(opponent) before had a better option earlier on in this depth the tree, don't bother continuing down this line of computing
            if (beta <= alpha):
    #           break
                break

    #       return the best possible move assuming that the opponent took the best move. (current_max_eval)
        return cur_max_eval
    #

    #If the current player is the one seeking the minimum evaluation:
    else:
    #   current_min_eval = infinity
        cur_min_eval = float("inf")
    #   new_frontier = expand(current node)
        new_frontier = treeRoot.expand()
    #   for each of the children in the frontier:
        for child in new_frontier:
    #       evaluation = minimax_pruned(cur_child, current depth - 1, alpha, beta, (true/false depending on next player in this position))
            next_player = True if (child.player == original) else False
            p_eval = minimax_pruned(child, cur_depth - 1, alpha, beta, next_player, original)
    #       current_min_eval = min(current_min_eval, evaluation)
            cur_min_eval = min(cur_min_eval, p_eval)
    #       beta = min(beta, evaluation)
            beta = min(beta, p_eval)
    #       if beta <= alpha: <-- which is to say, if the MAXIMIZER(opponent) before had a better option earlier on in this depth the tree, don't bother continuing down this line of computing
            if (beta <= alpha):
    #           break
                break
    #       return the best possible move assuming that the opponent took the best move. (current_min_eval) #
        return cur_min_eval

def score_monteCarlo(c_node, max_time, player): #Generates the cost of this node based on how well it does in a Monte-carlo sim TODO: Triple check to make sure everything is fleshed out.

    #Calculate the range of moves we can take (what numbers are considered valid moves)
    time_start = time.time()        #NOTE: We will probably want to see how many games that the algorithm can complete in x seconds...
    cur_time = 0
    sim_kernel = node(c_node.parent, c_node.player, c_node.state, c_node.mancalas)
    wins = 0
    games = 0

    #While we're within our max simulation time:
    while(cur_time <= max_time):
    #   set our 'simulation node's boardstate (sim kernel, bc that sounds cool) to be our base node's boardstate
        sim_kernel.state = c_node.state[:]
        sim_kernel.mancalas = c_node.mancalas[:]
    #   
    #   While we're within our time limit: (This loop is for a single game simulation)
        while(cur_time <= max_time):
    #       check board for any holes with 0 balls, avoid them.
            move_range = []
            row = 0 if(sim_kernel.player == 1) else 1

            for i in range(len(sim_kernel.state[row])):
                if (sim_kernel.state[row][i] > 0):
                    move_range.append(i+1)    #Accounts for move 0-indexing
            
    #       randomly generate an allowable move (exclude any 0-holes)
            move = move_range[random.randrange(0, len(move_range))]
    #       Generate boardstate after move, save it.
            results = sim_kernel.takeMove(move, sim_kernel.player)
            sim_kernel.state = results[0]
            sim_kernel.mancalas = results[1]
            sim_kernel.player = results[2]
    #       Evaluate the boardstate - is the game over?
            if (sim_kernel.evalBoard()):
                sim_kernel.mancalas[0] += sum(sim_kernel.state[0])
                sim_kernel.mancalas[1] += sum(sim_kernel.state[1])
    #       yes:
    #       Did we win? Update win rate of this node accordingly.
                if ((player == 1) and (sim_kernel.mancalas[0] > sim_kernel.mancalas[1])):
                    wins += 1
                    games += 1
                    break
    #       break from this current game loop.
                elif ((player == 1) and (sim_kernel.mancalas[0] < sim_kernel.mancalas[1])):
                    games += 1
                    break
                #       break from this current game loop.
                elif ((player == 2) and (sim_kernel.mancalas[0] < sim_kernel.mancalas[1])):
                    wins += 1
                    games += 1
                    break
                elif ((player == 2) and (sim_kernel.mancalas[0] > sim_kernel.mancalas[1])):
                    games += 1
                    break
                elif(sim_kernel.mancalas[0] == sim_kernel.mancalas[1]):
                    games += 1
                    break
            else:
                  
                cur_time = time.time() - time_start
    #           no:
    #               continue this game loop 
        cur_time = time.time() - time_start
    # 
    #Return the total winrate of this node#
    return (wins/games)
