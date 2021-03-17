#!/usr/bin/python
class Case:

    ##################################################################################
    #######################   EXPLANATIONS ABOUT THIS CLASS    #######################

    ## Here are explanations


    ##################################################################################
    #######################         CLASS CONSTRUCTOR          #######################

    def __init__(self, coordinate, zone):
        self.center = coordinate
        self.zone = zone
        self.visited = False


    ##################################################################################
    #######################              GETTERS               #######################

    # Get Coordinates (Coordinate class)
    def getCenter(self):
        return self.center
    
    # Get Zone (Zone class)
    def getZone(self):
        return self.zone

    # Get Visited (bool)
    def isVisited(self):
        return self.visited


    ##################################################################################
    #######################              SETTERS               #######################

    # Set Center (Coordinate class)
    def setCenter(self, coordinate):
        self.center = coordinate
    
    # Set Zone (float)
    def setZone(self, zone):
        self.zone = zone

    # Set Visited (bool)
    def setVisited(self, visited):
        self.visited = visited


    ##################################################################################
    #######################       CLASS STRING FOR DEBUG       #######################

    def toString(self):
        return self.center.toString(), self.zone.toString(), self.visited


    ##################################################################################
    #######################             FUNCTIONS              #######################