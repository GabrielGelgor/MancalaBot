import math

class node:
    def __init__(self, parent, player, state):
        self.parent = parent
        self.player = player
        self.state = state                      #State of the board, includes scores for each player. Represented as 2d array
        self.value = float("-inf")

    def expand(self):
        #for every possible child
        for child in range(1, len(self.state[0])):
            break
            #calculate new board state from the current state. Base move on iterator  
            #for every marble in this hole:
                #
            #generate node using current player as parent, and state
            #Add node to frontier
        return 0

    def takeMove(self, move, player):
        cur_state = self.state[:]

        #Determine the row and direction for this move based on the player

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
        #Scan the current board, if it is in a win state, return so. Else, return not.
        end = false
        for i in range(len(self.state)) 
            if (i == 0):
                for j in range(len(self.state[i]))
                    if (self.state[i][j] != 0):
                        end = true
            if (i == 1):
                for j in range(len(self.state[i]))
                    if (self.state[i][j] != 0):
                        end = true
        return end

