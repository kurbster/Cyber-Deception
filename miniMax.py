import networkManager
import sys
import random

class MiniMaxAgent:
    def __init__(self, possibleOC, cost, depth=3):
        self.depth = depth
        self.osn = possibleOC
        self.maxCost = cost

    # This is the function that will return the utility
    # For a specific configuration
    def evaluationFunction(self, tc):
        return random.randint(2, 10)

    # This is the function that will implement the minimax algorithm
    # We will use the values from the evaluation function to do this
    def greedyMiniMax(self, tsn):
        # This will keep track of the lowest possible cost for masking that node
        minIndCost = {}
        for trueConfig in tsn:
            # Here I assign the utility for each tc by using the evaluation function
            trueConfig.utility = self.evaluationFunction(trueConfig)
            # I loop through each oc and get the minimum cost
            # minIndCost is a dictionary that stores the TC with the minimum cost
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
            currentUtilities = {}       # This is the current utilities for each OC
            # This is the current observed configurations which maps an OC to an int
            # The int represents how many of our TCs have been masked to this OC
            currentObserved = {}
            for oc in self.osn: currentObserved[oc] = 0
            # Here we want to initialize our strategy which right now it no deception at all
            # TODO should we add randomization here to get different results?
            strategy = {}
            for tc in tsn:
                for oc in self.osn:
                    # If the tc and the oc have the same OS then I set the strategy of that tc to that oc
                    # Giving us no deception right now
                    if tc.OS == oc.OS:
                        strategy[tc] = oc
                        currentObserved[oc] += 1

            for system in systemList:
                oldOS = strategy[system]
                # Assign a new OC to that system based off of the assign function
                strategy[system] = self.greedyMiniMaxAssign(system, strategy, currentObserved,
                                                            requiredB, remainingB, minIndCost)
                # If the new oc is different than the one before then we need to change the OSN
                if not oldOS.OS == strategy[system].OS:
                    currentObserved[oldOS] = currentObserved[oldOS] - 1
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
            # Here I am decrementing the number of times the current observedConfig is being used
            currentOSN[currentStrat[trueConfig]] = currentOSN[currentStrat[trueConfig]] - 1
            # Then I increment the current OSN for the oc we changed to
            currentOSN[observedConfig] = currentOSN[observedConfig] + 1
            # Then I change the deception then after find the new utility
            currentStrat[trueConfig] = observedConfig
            totalUtility = 0
            # I need to calculate the new utility based on this new configuration
            for tc in currentStrat.iterkeys():
                if currentStrat[tc] == observedConfig:
                    totalUtility += tc.utility
            # The new utility is the average of the utility of all
            # The TCs mapped to our OC, currentOSN saves the number of TCs mapped
            # To our OC but we just added another one to the system so I add by one
            newUtility[observedConfig] = self.systemUtility(currentStrat, currentOSN)
        bestOC = min(newUtility.items(), key=lambda x: x[1])
        return bestOC[0]

    def systemUtility(self, currentStrat, currentOSN):
        sysUtil = {}
        for oc in self.osn: sysUtil[oc] = 0
        totalUtil = 0
        for tc, oc in currentStrat.items():
            sysUtil[oc] += tc.utility
        for oc, utilities in sysUtil.items():
            if currentOSN[oc] == 0: continue
            totalUtil += utilities / currentOSN[oc]
        return totalUtil
    # This function should return the cost of masking the trueConfig to the observedConfig
    def cost(self, trueConfig, observedConfig):
        return random.randint(1, 10)


if __name__ == '__main__':
    # This would be our F in the game theory paper which is the true state of the network
    tsn = networkManager.createNetwork(sys.argv[1])
    # This is all possible observable configurations
    osn = networkManager.createOSN()
    maxCost = 6 * tsn.__len__()
    miniMax = MiniMaxAgent(osn, maxCost, 5)
    miniMax.greedyMiniMax(tsn)


