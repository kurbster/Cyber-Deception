class ObservedConfiguration:
    def __init__(self, os):
        self.os = os
        # This will hold the TCs this OC can mask
        self.masked = []


class TrueConfiguration:
    def __init__(self, name, os, utility):
        self.name = name
        self.OS = os
        self.utility = utility

# This method is passed in the manual input from the command line
# This it reads the file and creates the appropriate TCs
def createNetwork(inputFile, miniMaxClass):
    systems = []
    with open(inputFile, 'r') as f:
        for line in f:
            attributes = line.split(',')
            # The last attribute will have a newline character at the end of it so we remove it
            attributes[-1] = attributes[-1].strip("\n")
            systems.append(createConfiguration(attributes, miniMaxClass))
    return systems

# This will create a configuration with the given attributes with the utility being scored by our miniMaxClass
def createConfiguration(attributes, miniMaxClass):
    utility = miniMaxClass.evaluationFunction(attributes)
    config = TrueConfiguration(attributes[0], attributes[1], utility)
    return config


# Do we want the full list from CyberVAN
possibleOS = ['Mac', 'Windows', 'Linux']
def createOC():
    allOC = []
    for os in possibleOS:
        myOC = ObservedConfiguration(os)
        allOC.append(myOC)
    return allOC

def networkToText(tsn, osn):
    return 0









