import math

class node:
    def __init__(self, parent, player, state, mancalas):
        self.parent = parent
        self.player = player
        self.state = state                      #State of the board, excluding mancalas
        self.mancalas = mancalas                #Mancala array - 0 for player 1, 1 for player 2.
        self.value = float("-inf")

    def expand(self):
        #Define output list, called 'frontier'
        #Get the number of possible moves
        #Using current player, determine which row to take moves from

        #For the number of possible moves: <- move = iterator
        #   Take the move starting at position (move) in row (player_row)
        #   Save the return value of takeMove, separating out the new board state and who the next player will be.
        #   Use these values to generate a new child node. Append this to our output: frontier#

        #Return the new frontier!

        return 0

    def takeMove(self, move, player):
        cur_state = self.state[:]

        #Determine the row and direction for this move based on the player
        #Subtract 1 from move to bring it in line with 0 indexing

        #Remove all the marbles from the hole they were taken from
        #Add these marbles to your "hand" 
        #Set a counter for how many moves you've taken (start at 1)
        #while you still have marbles left in your hand:
        #   determine the position of where you should place the next marble{
        #   counter(holes traveled so far) * your direction + the original position of your hole.}
        # 
        #   Is this marble within your list? {
        #       yes (is destination between 0 and the last hole?): place the marble, no problem.
        # 
        #       no: row switch! do the following
        #           have you hit your mancala? check the row you just finished against the player. If yes, drop a marble. check if this is your last marble.
        #           switch your row
        #           switch your direction
        #           based on which row you just entered, place where your 'move' now originates from.
        #           set counter (i) to -1 so your displacement will end up starting at 0 when you go back to the top 
        #           }
        # 
        #   add one to displacement counter#

        #Return the new state, as well as the next player in the case of consecutive turns, return the side of the board you finally landed on.
        return 0

    def evalBoard(self): #Determine whether or not this board is in a win state
        #Scan the current board, if it is in a win state, return so. Else, return not. TODO: Refactor
        end = False
        for i in range(len(self.state)): 
            if (i == 0):
                for j in range(len(self.state[i])):
                    if (self.state[i][j] != 0):
                        end = True
            if (i == 1):
                for j in range(len(self.state[i])):
                    if (self.state[i][j] != 0):
                        end = True
        return end

