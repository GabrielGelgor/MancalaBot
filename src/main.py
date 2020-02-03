from structs import node
import math, time, random

#Read Input
player = int(input())
mancala1 = [int(input())]
mancala1_marbles = [int(i) for i in input().strip().split()]
mancala2 = [int(input())]
mancala2_marbles = [int(i) for i in input().strip().split()]
print(printNextMove(player, mancala1, mancala1_marbles, mancala2, mancala2_marbles))

#Main function
def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):  
    state1 = mancala1_marbles[:]
    state2 = mancala2_marbles[:] 
    boardState = [state1, state2]

    #TODO: Fuse mancals into single 1d list
    #TODO: Place Minimax here based off of initial board as root.
     
    print("output")


'''
Main function. A/B Pruning is a feature of our minimax costing algorithm, so let's just roll the two into a single function.
'''
def minimax_pruned(treeRoot, cur_depth, alpha, beta, maxer): #Recursively explores the tree, rating nodes as they are reached. If we reach a place where the tree can be pruned, then we do NOT rate it.
    #Alpha and beta can be considered as a 'give me a better price or leave' metric. If the minimizer has a beta and the maximizer provides something higher than it, the minimizer will ignore the bargain - and visa versa.
        #if beta is less than alpha, then the opposing party being offered this deal will NEVER want the deal as the lowest acceptable bondary has been crossed.

    #If (current depth = 0 (maximum depth to be allowed)) or (current game board is in a finished state):
    if (cur_depth == 0):
    #   If the board is in a finished state, set heuristic value to 100% win rate for that node
        if (treeRoot.evalBoard()):
            return 1

    #   Else run the heuristic function, returning that evaluation of the node.
        else:
            '''THIS IS WHERE WE KEEP THE HEURISTIC CALL'''
            return score_monteCarlo(treeRoot, 2, treeRoot.player)
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
            next_player = True if (child.player == 1) else False
            p_eval = minimax_pruned(child, cur_depth - 1, alpha, beta, next_player)
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
            next_player = True if (child.player == 1) else False
            p_eval = minimax_pruned(child, cur_depth - 1, alpha, beta, next_player)
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
        sim_kernel.state = c_node.state
        sim_kernel.mancalas = c_node.mancalas
    #   
    #   While we're within our time limit: (This loop is for a single game simulation)
        while(cur_time <= max_time):
    #       check board for any holes with 0 balls, avoid them.
            move_range = []
            row = 0 if(sim_kernel.player == 1) else 1

            for i in range(len(sim_kernel.state[row])):
                if (sim_kernel.state[row][i] > 0):
                    move_range.append(i+1)                              #Accounts for move 0-indexing
            
    #       randomly generate an allowable move (exclude any 0-holes)
             try:
                move = move_range[random.randrange(0, len(move_range))]
            except ValueError:
                return (wins / games)
    #       Generate boardstate after move, save it.
            results = sim_kernel.takeMove(move, player)
            sim_kernel.state = results[0]
            sim_kernel.mancalas = results[1]
            sim_kernel.player = results[2]
    #       Evaluate the boardstate - is the game over?
            if (sim_kernel.evalBoard()):
    #       yes:
    #       Did we win? Update win rate of this node accordingly.
                if ((player == 1) and (sim_kernel.mancalas[0] > sim_kernel.mancalas[1])):
                    wins += 1
                    games += 1
                    break
    #       break from this current game loop.
                elif ((player == 2) and (sim_kernel.mancalas[0] < sim_kernel.mancalas[1])): #TODO: do we not have to consider the case where the other player won the full game on your own move? 
                    wins += 1
                    games += 1
                    break
            else:
                games += 1  
                cur_time = time.time() - time_start
    #           no:
    #               continue this game loop 
        cur_time = time.time() - time_start
    # 
    #Return the total winrate of this node#
    return (wins/games)

def hScore(player, move, boardState): #TODO: Refactor

    #Calculate score difference between both players' mancala
    if (player == 1):
        H1 = mancala1 - mancala2
    if (player == 2):
        H1 = mancala2 - mancala1
        
    #Maximize counters on players own side of board
    if (player == 1): #If player 1 calculate number of counters on your side
        mySide = boardState[0][0] + boardState[0][1] + boardState[0][2] + boardState[0][3] + boardState[0][4] + boardState[0][5]
        otherSide = boardState[1][0] + boardState[1][1] + boardState[1][2] + boardState[1][3] + boardState[1][4] + boardState[1][5]
        H2 = mySide - otherSide
    if (player == 2): #else if player 2 determine the counters on their side 
        mySide = boardState[1][0] + boardState[1][1] + boardState[1][2] + boardState[1][3] + boardState[1][4] + boardState[1][5]
        otherSide = boardState[0][0] + boardState[0][1] + boardState[0][2] + boardState[0][3] + boardState[0][4] + boardState[0][5]
        H2 = mySide - otherSide

    #Calculate if you get an extra move
    H3 = 0
    if (player == 1): #if player 1, move distance to mancala = 0, set h3 to 1
        numOfMarbles = boardState[0][move]
    if (player == 2): #if player 2, move distance to mancala = 0, set h3 to 1
        numOfMarbles = boardState[1][move]
        


    #Try to end turn on an empty pit
    H4 = 0
    

#'''https://www.hackerrank.com/challenges/mancala6'''
#"https://github.com/naigutstein/Mancala/blob/master/Player.py" #ref guide i guess