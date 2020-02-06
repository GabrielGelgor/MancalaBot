import math, random, copy, time
class node:
    def __init__(self, parent, player, state, mancalas, moveTaken):
        self.parent = parent
        self.player = player
        self.state = state  # State of the board, excluding mancalas
        self.mancalas = mancalas  # Mancala array - 0 for player 1, 1 for player 2.
        self.value = float("-inf")
        self.moveTaken = moveTaken

    def expand(self):
        # Define output list, called 'frontier'
        frontier = []
        # Get the number of possible moves
        b = len(self.state[0])  # b = branching factor

        # For the number of possible moves: <- move = iterator
        for move in range(1, b+1):
            #   Take the move starting at position (move) in row (player_row)
            #   Save the return value of takeMove, separating out the new board state and who the next player will be.
            
            if self.player == 1:
                row = 1
            else:
                row = 0
            if(self.state[row][move-1] != 0):
                Move = self.takeMove(move, self.player)
                #   Use these values to generate a new child node. Append this to our output: frontier#
                frontier.append(node(self, copy.deepcopy(Move[2]), copy.deepcopy(Move[0]), copy.deepcopy(Move[1]), copy.deepcopy(Move[3])))

        # Return the new frontier!
        return frontier

    def takeMove(self, move, player):
        cur_state = copy.deepcopy(self.state[:])
        cur_mancala = copy.deepcopy(self.mancalas[:])

        # Determine the row and direction for this move based on the player
        row = 1 if (player == 1) else 0
        inc = -1 if (player == 2) else 1
        # Subtract 1 from move to bring it in line with 0 indexing
        indexed_move = move - 1

        # Remove all the marbles from the hole they were taken from
        # Add these marbles to your "hand"
        marbles = cur_state[row][indexed_move]
        cur_state[row][indexed_move] = 0
        # Set a counter for how many moves you've taken (start at 1)
        displacement = 1

        # while you still have marbles left in your hand:
        while (marbles > 0):
            #   determine the position of where you should place the next marble{
            #   counter(holes traveled so far) * your direction + the original position of your hole.}
            pointer_pos = (displacement * inc + indexed_move)
            #
            #   Is this marble within your list? {
            #       yes (is destination between 0 and the last hole?): place the marble, no problem.
            if ((pointer_pos >= 0) and (pointer_pos < len(cur_state[row]))):
                cur_state[row][pointer_pos] += 1
                marbles -= 1
                ownedrow = 1 if player == 1 else 0
                if (marbles == 0 and cur_state[row][pointer_pos] == 1 and (row == ownedrow)):
                    oppositerow = 1 if (row == 0) else 0
                    cur_state[row][pointer_pos] += cur_state[oppositerow][pointer_pos]
                    cur_state[oppositerow][pointer_pos] = 0
            #
            #       no: row switch! do the following
            else:
                #           have you hit your mancala? check the row you just finished against the player. If yes, drop a marble. check if this is your last marble.
                if ((player == 1 and row == 1) or (player == 2 and row == 0)):
                    if (player == 1):
                        cur_mancala[0] += 1
                    else:
                        cur_mancala[1] += 1

                    marbles -= 1

                    if (marbles == 0):
                        return (cur_state, cur_mancala, player, move)
                        #           switch your row
                    row = 1 if (row == 0) else 0
                    #           switch your direction
                    inc *= -1
                    #           based on which row you just entered, place where your 'move' now originates from.
                    indexed_move = 0 if (player == 2) else len(cur_state[row]) - 1
                    #           set counter (i) to -1 so your displacement will end up starting at 0 when you go back to the top
                    displacement = -1
                #           }
                elif (player == 1 and row == 0):
                    row = 1
                    inc *= -1
                    indexed_move = 0
                    displacement = -1
                elif (player == 2 and row == 1):
                    row = 0
                    inc *= -1
                    indexed_move = 5
                    displacement = -1
            #
            displacement += 1
        #   add one to displacement counter#
        if (player == 1):
            player = 2
        else:
            player = 1
        # Return the new state, as well as the next player in the case of consecutive turns, return the side of the board you finally landed on.
        return (cur_state, cur_mancala, player, move)

    def evalBoard(self):  # Determine whether or not this board is in a win state
        # Scan the current board, if it is in a win state, return so. Else, return not. TODO: Refactor
        end = False
        counterP1 = 0
        counterP2 = 0
        for i in range(len(self.state)):
            if (i == 0):
                for j in range(len(self.state[i])):
                    if (self.state[i][j] == 0):
                        counterP1 += 1
            if (i == 1):
                for j in range(len(self.state[i])):
                    if (self.state[i][j] == 0):
                        counterP2 += 1
        if (counterP1 == 6 or counterP2 == 6):
            end = True
        return end

def minimax_pruned(treeRoot, cur_depth, alpha, beta, maxer, original):  # Recursively explores the tree, rating nodes as they are reached. If we reach a place where the tree can be pruned, then we do NOT rate it.
    # Alpha and beta can be considered as a 'give me a better price or leave' metric. If the minimizer has a beta and the maximizer provides something higher than it, the minimizer will ignore the bargain - and visa versa.
    # if beta is less than alpha, then the opposing party being offered this deal will NEVER want the deal as the lowest acceptable bondary has been crossed.
    start_time = time.time()
    # If (current depth = 0 (maximum depth to be allowed)) or (current game board is in a finished state):
    if (cur_depth == 0):
        #   If the board is in a finished state, set heuristic value to 100% win rate for that node
        if (treeRoot.evalBoard()):
            winner = None
            if (treeRoot.mancalas[0] > treeRoot.mancalas[1]):
                winner = 1
            elif(treeRoot.mancalas[1] > treeRoot.mancalas[0]):
                winner = 2
            else:
                winner = 0
            if (winner == original):
                return (0.5, None)
            else:
                return (-0.5, None)

        #   Else run the heuristic function, returning that evaluation of the node.
        else:
            '''THIS IS WHERE WE KEEP THE HEURISTIC CALL'''
            heuristic = score_monteCarlo(treeRoot, 0.15, treeRoot.player)  # NOTE: might need to tweak time
            if (treeRoot.player == original):
                return ((heuristic - 0.5), None)
            else:
                return ((0.5 - heuristic), None)  # as 0.5 is the same winning chance for both players, we base our score off of how close/far we are from the 0.5 index
    #
    # If the current player is the one seeking the maximum evaluation:
    if (maxer):
        #   current_max_eval = -infinity
        cur_max_eval = float("-inf")
        maxMove = None
        #   new_frontier = expand(current node)
        new_frontier = treeRoot.expand()
        #   for each of the children in the frontier:
        for child in range(len(new_frontier)):
            #       evaluation = minimax_pruned(cur_child, current depth - 1, alpha, beta, (true/false depending on next player in this position))
            next_player = True if (new_frontier[child].player == original) else False
            p_eval = (minimax_pruned(new_frontier[child], cur_depth - 1, alpha, beta, next_player, original))[0]
            #       current_max_eval = max(current_max_eval, evaluation)
            cur_max_eval = max(cur_max_eval, p_eval)
            #       alpha = max(alpha, evaluation)
            if (p_eval >= alpha):    #Adding 1 to bring it up to nonindex move
                maxMove = new_frontier[child].moveTaken
            alpha = max(alpha, p_eval)
            #       if beta <= alpha: <-- which is to say, if the MINIMIZER(opponent) before had a better option earlier on in this depth the tree, don't bother continuing down this line of computing
            if (beta <= alpha):
                #           break
                break

        #       return the best possible move assuming that the opponent took the best move. (current_max_eval)
        return cur_max_eval, maxMove
    #

    # If the current player is the one seeking the minimum evaluation:
    else:
        #   current_min_eval = infinity
        cur_min_eval = float("inf")
        minMove = None
        #   new_frontier = expand(current node)
        new_frontier = treeRoot.expand()
        #   for each of the children in the frontier:
        for child in range(len(new_frontier)):
            #       evaluation = minimax_pruned(cur_child, current depth - 1, alpha, beta, (true/false depending on next player in this position))
            next_player = True if (new_frontier[child].player == original) else False
            p_eval = (minimax_pruned(new_frontier[child], cur_depth - 1, alpha, beta, next_player, original))[0]
            #       current_min_eval = min(current_min_eval, evaluation)
            cur_min_eval = min(cur_min_eval, p_eval)
            #       beta = min(beta, evaluation)
            if(p_eval <= beta):
                minMove = new_frontier[child].moveTaken #Adding 1 to bring it up to nonindex move
            beta = min(beta, p_eval)
            #       if beta <= alpha: <-- which is to say, if the MAXIMIZER(opponent) before had a better option earlier on in this depth the tree, don't bother continuing down this line of computing
            if (beta <= alpha):
                #           break
                break
        #       return the best possible move assuming that the opponent took the best move. (current_min_eval) #
        return cur_min_eval, minMove


def score_monteCarlo(c_node, max_time,player):  # Generates the cost of this node based on how well it does in a Monte-carlo sim TODO: Triple check to make sure everything is fleshed out.

    # Calculate the range of moves we can take (what numbers are considered valid moves)
    time_start = time.time()  # NOTE: We will probably want to see how many games that the algorithm can complete in x seconds...
    cur_time = 0
    sim_kernel = node(c_node.parent, c_node.player, c_node.state, c_node.mancalas, c_node.moveTaken)
    wins = 0
    games = 0
    # While we're within our max simulation time:
    while (cur_time <= max_time):
        #   set our 'simulation node's boardstate (sim kernel, bc that sounds cool) to be our base node's boardstate
        sim_kernel.state = c_node.state[:]
        sim_kernel.mancalas = c_node.mancalas[:]
        #
        #   While we're within our time limit: (This loop is for a single game simulation)
        while (cur_time <= max_time):
            #       check board for any holes with 0 balls, avoid them.
            move_range = []
            row = 0 if (sim_kernel.player == 2) else 1

            for i in range(len(sim_kernel.state[row])):
                if (sim_kernel.state[row][i] > 0):
                    move_range.append(i + 1)  # Accounts for move 0-indexing

            #       randomly generate an allowable move (exclude any 0-holes)
            move = move_range[random.randrange(0, len(move_range))]
            #       Generate boardstate after move, save it.
            results = sim_kernel.takeMove(move, sim_kernel.player)
            sim_kernel.state = results[0]
            sim_kernel.mancalas = results[1]
            sim_kernel.player = results[2]
            #       Evaluate the boardstate - is the game over?
            if (sim_kernel.evalBoard()):
                sim_kernel.mancalas[0] += sum(sim_kernel.state[1])
                sim_kernel.mancalas[1] += sum(sim_kernel.state[0])
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
    # Return the total winrate of this node#
    return (wins / games)


def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):
    bottomRow = player1Marbles[:]
    topRow = player2Marbles[:]
    boardState = [topRow, bottomRow]
    mancalas = [player1Mancala, player2Mancala]
    treeRoot = node(None, player, boardState, mancalas, None)
    cur_max_eval = float("-inf")
    cur_min_eval = float("inf")
    maxer = True
    original = player
    minimax = minimax_pruned(treeRoot, 2, cur_max_eval, cur_min_eval, maxer, original)
    # Send our player number to minimax as we are the original and we hardcode that we are maxer
    returnedVal = minimax[1]
    return(returnedVal)

# Read Input
inputPlayer = int(input())
mancala1 = int(input())
mancala1_marbles = [int(i) for i in input().strip().split()]
mancala2 = int(input())
mancala2_marbles = [int(i) for i in input().strip().split()]
print(printNextMove(inputPlayer, mancala1, mancala1_marbles, mancala2, mancala2_marbles))