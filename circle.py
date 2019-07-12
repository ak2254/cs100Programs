import point

class Circle:
    def __int__(self, center, radius):
        self.center=center
        self.radius=radius
    def area(self):
        import math
        area = math.pi *self.radius**2
        return area
    def circumference(self):
        return 2*math.Pi*self.radius
    def liesOnCircle(self, otherP):
        if otherP.distanceTo(self) == self.radius:
            return True
        else:
            return False
    
    
