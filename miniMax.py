class MiniMaxAgent:
    def __init__(self, depth=3):
        self.depth = depth

    # This is the function that will return the utility
    # For a specific configuration
    def evaluationFunction(self):
        return 0

    # This is the function that will implement the minimax algorithm
    # We will use the values from the evaluation function to do this
    def miniMaxTree(self):
        for i in range(20):
            print i


if __name__ == '__main__':
    miniMax = MiniMaxAgent()
    miniMax.miniMaxTree()