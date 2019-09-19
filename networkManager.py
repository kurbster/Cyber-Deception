class ObservedConfiguration:
    def __init__(self, os):
        self.os = os
        # This will hold the TCs this OC can mask
        self.masked = []


class TrueConfiguration:
    def __init__(self, name, os):
        self.name = name
        self.OS = os
        self.utility = 0


# This method is passed in the manual input from the command line
# This it reads the file and creates the appropriate TCs
def createNetwork(inputFile):
    systems = []
    with open(inputFile, 'r') as f:
        for line in f:
            attributes = line.split(',')
            # The last attribute will have a newline character at the end of it so we remove it
            attributes[-1] = attributes[-1].strip("\n")
            systems.append(createConfiguration(attributes))
    return systems


# This will create a configuration with the given attributes with the utility being scored by our miniMaxClass
def createConfiguration(attributes):
    return TrueConfiguration(attributes[0], attributes[1])


# Do we want the full list from CyberVAN
possibleOS = ['Mac', 'Windows', 'Linux']
def createOSN():
    allOC = []
    for os in possibleOS:
        myOC = ObservedConfiguration(os)
        allOC.append(myOC)
    return allOC


def networkToText(tsn, osn):
    return 0









