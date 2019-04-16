import random


class ObservedConfiguration:
    def __init__(self, os, web):
        self.os = os
        self.web = web
        # This will hold the TCs this OC can mask
        self.masked = []



class TrueConfiguration:
    def __init__(self, os, web, ssh, files, utility):
        self.os = os
        self.web = web
        self.SSH = ssh
        self.files = files
        self.utility = utility

# This method is passed in the manual input from the command line
# This it reads the file and creates the appropriate TCs
def createNetwork(inputFile):
    systems = []
    with open(inputFile, 'r') as f:
        for line in f:
            attributes = line.split(',')
            # The last attribute will have a newline character at the end of it
            # Unless it is the last system in the configuration, here we remove it
            attributes[3] = attributes[3].replace('\n', '')
            systems.append(createConfiguration(attributes))
    return systems


def createConfiguration(attributes):
    # As of right now I assign random utilities to each TC
    utility = random.randint(2, 10)
    config = TrueConfiguration(attributes[0], attributes[1], attributes[2], attributes[3], utility)
    return config

# Do we want the full list from CyberVAN
possibleOS = ['Mac', 'Windows', 'Linux']
# I don't know about this I went to this website
# https://www.tutorialspoint.com/web_developers_guide/web_server_types.htm
possibleWebServers = ['Tomcat', 'IIS', 'lighttpd', 'Sun Java', 'Jigsaw', 'nginx']
def createOC():
    allOC = []
    for os in possibleOS:
        for web in possibleWebServers:
            myOC = ObservedConfiguration(os, web)
            allOC.append(myOC)
    return allOC











