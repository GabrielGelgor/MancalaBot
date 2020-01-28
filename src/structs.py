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
        cur_mancala = self.mancalas[:]

        #Determine the row and direction for this move based on the player
        row = 0 if (player == 1) else 1
        inc = -1 if (player == 1) else 1
        #Subtract 1 from move to bring it in line with 0 indexing
        indexed_move = move - 1

        #Remove all the marbles from the hole they were taken from TODO: Check to see if there is nothing in that hole
        #Add these marbles to your "hand" 
        marbles = cur_state[row][indexed_move]
        cur_state[row][indexed_move] = 0
        #Set a counter for how many moves you've taken (start at 1)
        displacement = 1

        #while you still have marbles left in your hand:
        while (marbles > 0):
        #   determine the position of where you should place the next marble{
        #   counter(holes traveled so far) * your direction + the original position of your hole.}
            pointer_pos = (displacement * inc + indexed_move)
        # 
        #   Is this marble within your list? {
        #       yes (is destination between 0 and the last hole?): place the marble, no problem.
            if ((pointer_pos >= 0) and (pointer_pos <= len(cur_state[row]))):
                cur_state[row][pointer_pos] += 1
                marbles -= 1
        # 
        #       no: row switch! do the following
            else:
        #           have you hit your mancala? check the row you just finished against the player. If yes, drop a marble. check if this is your last marble.
                if ((player == 1 and row == 0) or (player == 2 and row == 1)):
                    if (player == 1):
                        cur_mancala[0] += 1
                    else:
                        cur_mancala[1] += 1
                    
                    marbles -= 1

                    if (marbles == 0):
                        pass #TODO: add in double turn feature, as well as feature for dropping last ball in empty hole
        #           switch your row
                    row = 1 if (row == 0) else 0 
        #           switch your direction
                    inc *= -1
        #           based on which row you just entered, place where your 'move' now originates from.
                    indexed_move = len(cur_state[row]) if (player == 1) else 0
        #           set counter (i) to -1 so your displacement will end up starting at 0 when you go back to the top 
                    displacement = -1
        #           }
        # 
            displacement += 1
        #   add one to displacement counter#

        #Return the new state, as well as the next player in the case of consecutive turns, return the side of the board you finally landed on.
        return (cur_state, cur_mancala, player, row) #TODO: Make sure that a varaibble keeps track of which is the next player.

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

