from structs import node
import math

#Read Input
player = int(input())
mancala1 = [int(input())]
mancala1_marbles = [int(i) for i in raw_input().strip().split()]
mancala2 = [int(input())]
mancala2_marbles = [int(i) for i in raw_input().strip().split()]
print(printNextMove(player, mancala1, mancala1_marbles, mancala2, mancala2_marbles))

#Main function
def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):  
    state1 = mancala1_marbles[:]
    state2 = mancala2_marbles[:] 
    boardState = [state1, state2]
    
    
    print("output")


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

def abPrune(node):# send in self, board, ply
    

    
    return 0

def hScore(player, move): 

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
        if ()
    if (player == 2): #if player 2, move distance to mancala = 0, set h3 to 1
        numOfMarbles = boardState[1][move]
        


    #Try to end turn on an empty pit
    H4 = 0
    

#'''https://www.hackerrank.com/challenges/mancala6'''
#"https://github.com/naigutstein/Mancala/blob/master/Player.py" #ref guide i guess