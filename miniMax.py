import util
import sys

class MiniMaxAgent:
    def __init__(self, depth=3):
        self.depth = depth

    # This is the function that will return the utility
    # For a specific configuration
    def evaluationFunction(self):
        return 0

    # This is the function that will implement the minimax algorithm
    # We will use the values from the evaluation function to do this
    def miniMax(self):
        return 0


if __name__ == '__main__':
    networkConfig = []
    # The default minimax depth is 3
    miniMax = MiniMaxAgent()
    # This would be our F in the game theory paper which is the true state of the network
    tsn = util.createNetwork(sys.argv[1])
    osn = util.createOC()


