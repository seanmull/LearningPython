from math import sqrt
from math import pi
class Line(object):
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        X = pow(self.coor2[0] - self.coor1[0], 2)
        Y = pow(self.coor2[1] - self.coor1[1], 2)
        return sqrt(X + Y) 

    def slope(self):
       diffX =  self.coor2[0] - self.coor1[0]
       diffY =  self.coor2[1] - self.coor1[1]
       return diffY / diffX

li = Line((3,2),(8,10))
print(li.distance())
print(li.slope())

class Cylinder(object):

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
    def volume(self):
        return pi * pow(self.radius,2) * self.height
    def surface_area(self):
        return 2*pi*self.radius*(self.height + self.radius) 

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())