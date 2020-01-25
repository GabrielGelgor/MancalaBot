from structs import node

#Main function
def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):
    print ""

#Read Input
player = input()
mancala1 = input()
mancala1_marbles = [int(i) for i in raw_input().strip().split()]
mancala2 = input()
mancala2_marbles = [int(i) for i in raw_input().strip().split()]
print printNextMove(player, mancala1, mancala1_marbles, mancala2, mancala2_marbles)

'''
HERE IS WHERE THE MAIN GAME LOOP WILL GO
COPIED FROM HACKERRANK

'''

def score_monteCarlo(node): #Generates the cost of this node based on how well it does in a Monte-carlo sim
    #While(within time limit)
    #   sim_node.boardstate = node.boardstate <-- Create simulation node? Like a kernel.
    #   while(board not in a win state and within time limit): 
    #       sim_node.take_move(random_move)
    #       result = sim_node.Eval_board()
    # 
    #       if (game over):
    #           if (won):
    #               update win rate accordingly
    #           else:
    #               do the same but for loss
    #           break #
    return 0

def abPrune(node):
    return 0

def hScore(): 
    # 1. My vs other mancala
    # 2. Empty node (don't pick)
    # 3. Keep as many counters on players side of board
    # 4. Allow for an extra move