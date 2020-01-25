import math

class node:
    def __init__(self, parent, player, state):
        self.parent = parent
        self.player = player
        self.state = state                      #State of the board, includes scores for each player. Represented as 2d array
        self.value = float("-inf")

    def expand(self):
        #for every possible child
            #calculate new board state from the current state. Base move on iterator
            #generate node using current player as parent, and state
            #Add node to frontier
        return 0

    def takeMove(self, move, player):
        #for the number of marbles in the selected hole
            #drop a marble in the next hole.
        
        #Is the first hole index + number of marbles your mancala?
            #If so, ensure that you get an extra turn

        #Return the new state, as well as the next player in the case of consecutive turns
        return 0

    def evalBoard(self): #Determine whether or not this board is in a win state
        #Scan the current board, if it is in a win state, return so. Else, return not.
        return 0

