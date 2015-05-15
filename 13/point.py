from math import sqrt # Need only sqrt from math package
import matplotlib.pyplot as plt

# Create a Point class, which will create a point object in the xy-plane.
class Point(object):

    # This is the constructor, which takes in an x and y coordinate. For
    # example, Point(2, 3) will create an instance for x = 2 and y = 3.
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Initialized distance. Updates when this variable is referenced.
        self.dist = 0 
    
    # Returns the x-value of the point.
    def getX(self):
        return self.x
        
    # Returns the y-value of the point.
    def getY(self):
        return self.y
    
    # Returns the point as a list of two values: the x and y-value 
    # respectively.
    def getPoint(self):
        return [self.x, self.y]
    
    # Returns the point in string representation.
    def toString(self):
        return "x = %s, y = %s" %(str(self.x), str(self.y))
    
    # Takes in a change-in-x and change-in-y and returns the new point as
    # a list.
    def translate(self, dx, dy):
        return [self.x + dx, self.y + dy]
    
    # Takes in a change-in-x and change-in-y and returns the moved point 
    # as a list.This is different than the translate method because self.x 
    # and self.y are storing new values.
    def movePoint(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return [self.x, self.y]
    
    # Takes in new x and y-values. Updates the instance variables and returns
    # the new x and y-values as a list.
    def movePoint2(self, newX, newY):
        self.x = newX
        self.y = newY
        return [self.x, self.y]
      
    # Takes in a and b to scale x and y-values respectively, and returns result
    # as a list.
    def scale(self, a, b):
        scaleX = a*self.x
        scaleY = b*self.y
        return [scaleX, scaleY]
    
    # Returns the distance from origin. No instance variables are updated.
    def distanceFromOrigin(self):
        dist = sqrt(self.x**2 + self.y**2)
        return dist
    
    # Returns the distance from another point. You can actually pass in
    # objects - the parameter other is just another instance of this class.
    def distance(self, other):
        dx = self.x - other.getX()
        dy = self.y - other.getY()
        self.dist = sqrt(dx**2 + dy**2)
        return self.dist
     
    # Returns midpoint using another point. This time a new point object
    # is returned.
    def midpoint(self, other):
        midX = (self.x + other.getX())/2
        midY = (self.y + other.getY())/2
        return Point(midX, midY)
    
    # Plots a point as red dot.
    def plotPoint(self):
        plt.plot(self.x, self.y, 'ro')
        
# Test some of the methods!     
newPoint = Point(2, 3) # Creates an instance.
print newPoint.getPoint() # Returns [2, 3] as list.

print newPoint.translate(1, 1) # Returns [3, 4] as list.
print newPoint.getX() # Returns x-value of 2 because self.x was not updated.

print newPoint.movePoint2(10, 10) # Moves point to [10, 10] as list.

# Expresses point as string (x = 10, y = 10) because both instance variables
# are updated.
print newPoint.toString() 

otherPoint = Point(1, 1) # Creates another instance.
print newPoint.distance(otherPoint) # Distance between newPoint and otherPoint.

# Returns midpoint of newPoint and otherPoint.
print newPoint.midpoint(otherPoint).getPoint()

# Plots the point.
newPoint.plotPoint()