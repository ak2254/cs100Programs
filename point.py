class Point:
    def __init__(self, xcoor, ycoor):
        self.x = xcoor
        self.y = ycoor
    def coordinates(self):
        ''' Return a tuple of the x,y coordinates of a point '''
        return (self.x, self.y)
    def moveTo(self, xcoor, ycoor):
        ''' Assign new coordinates to a point '''
        self.x = xcoor
        self.y = ycoor
    def distanceTo(self, other):
        import math
        distance = math.sqrt((self.x - other.x) **2 + (self.y - other.y) **2)
        return distance
