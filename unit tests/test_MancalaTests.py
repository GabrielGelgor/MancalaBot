from unittest import TestCase
import MancalaTests


class Test(TestCase):
    def test_eval_board_gameEnd(self):
        self.state = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        self.assertEqual(MancalaTests.evalBoard(self, self.state), True)

    def test_eval_board_gameNotEnd(self):
        self.state = [[4, 4, 4, 4, 4, 4], [0, 0, 0, 0, 0, 0]]
        self.assertEqual(MancalaTests.evalBoard(self, self.state), False)

    # Test player 1: move 6
    def test_takeMove11(self):
        self.state = [[4, 4, 4, 4, 4, 4], [0, 0, 0, 0, 0, 0]]
        self.mancalas = [0, 0]
        self.player = 1
        self.move = 6
        newState, newMancalas, newMove, newPlayer =  MancalaTests.takeMove(self, self.move, self.player, self.state, self.mancalas)
        self.assertEqual(newState, [[4, 5, 5, 5, 5, 0], [0, 0, 0, 0, 0, 0]])
        self.assertEqual(newMancalas, [0, 0])

    # Test player 1: move 4
    def test_takeMove12(self):
        self.state = [[4, 4, 4, 4, 4, 4], [0, 0, 0, 0, 0, 0]]
        self.mancalas = [0, 0]
        self.player = 1
        self.move = 4
        newState, newMancalas, newMove, newPlayer = MancalaTests.takeMove(self, self.move, self.player, self.state, self.mancalas)
        self.assertEqual(newState, [[5, 5, 5, 0, 4, 4], [0, 0, 0, 0, 0, 0]])
        self.assertEqual(newMancalas, [1, 0])


    # Test player 1: move 6
    def test_takeMove14(self):
        self.state = [[20, 20, 20, 20, 20, 20], [20, 20, 20, 20, 20, 20]]
        self.mancalas = [0, 0]
        self.player = 1
        self.move = 6
        newState, newMancalas, newMove, newPlayer = MancalaTests.takeMove(self, self.move, self.player, self.state, self.mancalas)
        self.assertEqual(newState, [[22, 22, 22, 22, 22, 1], [22, 21, 21, 21, 21, 21]])
        self.assertEqual(newMancalas, [2, 0])

    # Test player 1: move 3
    def test_takeMove15(self):
        self.state = [[35, 35, 35, 35, 35, 35], [35, 35, 35, 35, 35, 35]]
        self.mancalas = [0, 0]
        self.player = 1
        self.move = 3
        newState, newMancalas, newMove, newPlayer = MancalaTests.takeMove(self, self.move, self.player, self.state, self.mancalas)
        self.assertEqual(newState, [[38, 38, 2, 37, 37, 37], [38, 38, 38, 38, 38, 38]])
        self.assertEqual(newMancalas, [3, 0])

    # Test player 2: move 6
    def test_takeMove21(self):
        self.state = [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4]]
        self.mancalas = [0, 0]
        self.player = 2
        self.move = 6
        newState, newMancalas, newMove, newPlayer = MancalaTests.takeMove(self, self.move, self.player, self.state, self.mancalas)
        self.assertEqual(newState, [[4, 4, 4, 5, 5, 5], [4, 4, 4, 4, 4, 0]])
        self.assertEqual(newMancalas, [0, 1])

    # Test player 2: move 1
    def test_takeMove22(self):
        self.state = [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4]]
        self.mancalas = [0, 0]
        self.player = 2
        self.move = 1
        newState, newMancalas, newMove, newPlayer = MancalaTests.takeMove(self, self.move, self.player, self.state, self.mancalas)
        self.assertEqual(newState, [[4, 4, 4, 4, 4, 4], [0, 5, 5, 5, 5, 4]])
        self.assertEqual(newMancalas, [0, 0])

    # Test player 2: move 6
    def test_takeMove13(self):
        self.state = [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4]]
        self.mancalas = [0, 0]
        self.player = 2
        self.move = 6
        newState, newMancalas, newMove, newPlayer = MancalaTests.takeMove(self, self.move, self.player, self.state,
                                                                          self.mancalas)
        self.assertEqual(newState, [[4, 4, 4, 5, 5, 5], [4, 4, 4, 4, 4, 0]])
        self.assertEqual(newMancalas, [0, 1])

    # Test player 2: move 6
    def test_takeMove23(self):
        self.state = [[20, 20, 20, 20, 20, 20], [20, 20, 20, 20, 20, 20]]
        self.mancalas = [0, 0]
        self.player = 2
        self.move = 6
        newState, newMancalas, newMove, newPlayer = MancalaTests.takeMove(self, self.move, self.player, self.state, self.mancalas)
        self.assertEqual(newState, [[22, 22, 22, 22, 22, 22], [21, 21, 21, 21, 21, 1]])
        self.assertEqual(newMancalas, [0, 2])

    # Test player 2: move 3
    def test_takeMove24(self):
        self.state = [[35, 35, 35, 35, 35, 35], [35, 35, 35, 35, 35, 35]]
        self.mancalas = [0, 0]
        self.player = 2
        self.move = 3
        newState, newMancalas, newMove, newPlayer = MancalaTests.takeMove(self, self.move, self.player, self.state, self.mancalas)
        self.assertEqual(newState, [[37, 38, 38, 38, 38, 38], [37, 37, 2, 38, 38, 38]])
        self.assertEqual(newMancalas, [0, 3])

