from structs import node
import math

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

    #TODO: Place Minimax here based off of initial board as root.
     
    print("output")


'''
Main function. A/B Pruning is a feature of our minimax costing algorithm, so let's just roll the two into a single function.
'''
def minimax_pruned(treeRoot, max_depth, alpha, beta, maxer): #Recursively explores the tree, rating nodes as they are reached. If we reach a place where the tree can be pruned, then we do NOT rate it.
    #Alpha and beta can be considered as a 'give me a better price or leave' metric. If the minimizer has a beta and the maximizer provides something higher than it, the minimizer will ignore the bargain - and visa versa.
        #if beta is less than alpha, then the opposing party being offered this deal will NEVER want the deal as the lowest acceptable bondary has been crossed.

    #If (current depth = 0 (maximum depth to be allowed)) or (current game board is in a finished state):
    #   If the board is in a finished state, set heuristic value to 100% win rate for that node
    #   Else run the heuristic function, returning that evaluation of the node.
    # 
    #If the current player is the one seeking the maximum evaluation:
    #   current_max_eval = -infinity
    #   new_frontier = expand(current node)
    #   for each of the children in the frontier:
    #       evaluation = minimax_pruned(cur_child, current depth - 1, alpha, beta, (true/false depending on next player in this position))
    #       current_max_eval = max(current_max_eval, evaluation)
    #       alpha = max(alpha, evaluation)
    #       if beta <= alpha: <-- which is to say, if the MINIMIZER(opponent) before had a better option earlier on in this depth the tree, don't bother continuing down this line of computing
    #           break
    #       return the best possible move assuming that the opponent took the best move. (current_max_eval)
    #
    #If the current player is the one seeking the minimum evaluation:
    #   current_min_eval = infinity
    #   new_frontier = expand(current node)
    #   for each of the children in the frontier:
    #       evaluation = minimax_pruned(cur_child, current depth - 1, alpha, beta, (true/false depending on next player in this position))
    #       current_min_eval = min(current_min_eval, evaluation)
    #       beta = min(beta, evaluation)
    #       if beta <= alpha: <-- which is to say, if the MAXIMIZER(opponent) before had a better option earlier on in this depth the tree, don't bother continuing down this line of computing
    #           break
    #       return the best possible move assuming that the opponent took the best move. (current_min_eval) #
    
    
    return 0

def score_monteCarlo(node, max_time): #Generates the cost of this node based on how well it does in a Monte-carlo sim

    #Calculate the range of moves we can take (what numbers are considered valid moves)
    #While we're within our max simulation time:
    #   set our 'simulation node's boardstate (sim kernel, bc that sounds cool) to be our base node's boardstate
    #   
    #   While we're within our time limit: (This loop is for a single game simulation)
    #       check board for any holes with 0 balls, avoid them.
    #       randomly generate an allowable move (exclude any 0-holes)
    #       Generate boardstate after move, save it.
    #       Evaluate the boardstate - is the game over?
    #           yes:
    #               Did we win? Update win rate of this node accordingly.
    #               break from this current game loop.
    #           no:
    #               continue this game loop 
    # 
    #Return the total winrate of this node#
    return 0

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