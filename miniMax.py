import networkManager
import fileManager
import sys
import random

class MiniMaxAgent:
    def __init__(self, possibleobserved, cost, depth=3):
        self.depth = depth
        self.osn = possibleobserved
        self.maxCost = cost

    # This is the function that will return the utility
    # For a specific configuration
    def evaluationFunction(self):
        return 0

    # This is the function that will implement the minimax algorithm
    # We will use the values from the evaluation function to do this
    def greedyMiniMax(self, tsn):
        # This will keep track of the lowest possible cost for masking that node
        minIndCost = {}
        for trueConfig in tsn:
            # I loop through each oc and get the minimum cost
            # minIndCost is a dictionary that store the TC with the minimum cost
            minIndCost[trueConfig] = min(self.cost(trueConfig, oc) for oc in self.osn)
        # This is the minimum cost to mask all systems
        minTotCost = sum(minIndCost.itervalues())
        # This is our final output strategy and the utility associated with it
        # The strategy is a dictionary with the TC as keys and OC as values
        bestCost = 0
        bestStrategy = {}
        for x in range(self.depth):
            systemList = tsn
            remainingB = self.maxCost   # The remaining cost we can allocate
            requiredB = minTotCost      # The required i.e minimum cost to mask all systems
            strategy = {}               # This is our strategy for out current iteration
            currentObserved = {}        # This is our current OSN, which is a dict mapping f~ to an int
            currentUtilities = {}       # This is the current utilities for each OC
            for i in range(systemList.__len__()):
                system = systemList[i]  # Get a TC from the list of systems
                # Assign a new OC to that system
                strategy[system] = self.greedyMiniMaxAssign(system, strategy, currentObserved,
                                                            requiredB, remainingB, minIndCost)
                # Increment the number instances for that OC
                currentObserved[strategy[system]] = currentObserved[strategy[system]] + 1
                remainingB = remainingB - self.cost(system, strategy[system])
                requiredB = requiredB - minIndCost[system]
        # TODO add in the update method for utility and the strategy which should complete the algorithm
        return bestStrategy

    def greedyMiniMaxAssign(self, trueConfig, currentStrat, currentOSN, reqB, remB, minIndCost):
        newUtility = {}
        # I consider every possible OC
        for observedConfig in self.osn:
            # I skip over any OC that would put us over the cost limit
            if reqB - minIndCost[trueConfig] + self.cost(trueConfig, observedConfig) > remB:
                continue
            currentStrat[trueConfig] = observedConfig
            totalUtility = 0
            # I need to calculate the new utility based on this new configuration
            for tc in currentStrat.iterkeys():
                if currentStrat[tc] == observedConfig:
                    totalUtility += tc.utility
            # The new utility is the average of the utility of all
            # The TCs mapped to our OC, currentOSN saves the number of TCs mapped
            # To our OC but we just added another one to the system so I add by one
            newUtility[observedConfig] = totalUtility / (currentOSN[observedConfig] + 1)
        minIndex = newUtility.values().index(min(newUtility.values()))
        bestOC = newUtility[minIndex][0]    # This returns the OC with the best, smallest,  utility
        return bestOC

    def cost(self, trueConfig, observedConfig):
        return random.randint(1, 10)


if __name__ == '__main__':
    # This would be our F in the game theory paper which is the true state of the network
    tsn = networkManager.createNetwork(sys.argv[1])
    osn = networkManager.createOC()
    maxCost = 6 * tsn.__len__()
    miniMax = MiniMaxAgent(osn, maxCost, 5)
    miniMax.greedyMiniMax(tsn)


