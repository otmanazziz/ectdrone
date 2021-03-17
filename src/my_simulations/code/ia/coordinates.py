#!/usr/bin/python
class Coordinates:

    ##################################################################################
    #######################   EXPLANATIONS ABOUT THIS CLASS    #######################

    ## Here are explanations


    ##################################################################################
    #######################         CLASS CONSTRUCTOR          #######################

    def __init__(self, x, y):
        self.x = x + 0.0
        self.y = y + 0.0


    ##################################################################################
    #######################              GETTERS               #######################

    # Get X coordinates (float)
    def getX(self):
        return self.x
    
    # Get Y coordinates (float)
    def getY(self):
        return self.y


    ##################################################################################
    #######################              SETTERS               #######################

    # Set Y coordinates (float)
    def setX(self, x):
        self.x = x + 0.0

    # Set X coordinates (float)
    def setY(self, y):
        self.y = y + 0.0


    ##################################################################################
    #######################       CLASS STRING FOR DEBUG       #######################

    def toString(self):
        return 'Coordinates:', [self.x, self.y]


    ##################################################################################
    #######################             FUNCTIONS              #######################