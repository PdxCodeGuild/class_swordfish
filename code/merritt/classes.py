import math, random

class Point:
    def __init__(self, x, y): # this is the initializer
        self.x = x # these are member variables
        self.y = y

    pi = 3.1415

    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)

    def scale(self, v):
        self.x *= v
        self.y *= v

    @staticmethod
    def from_polar(r, theta): # static methods belong to the type, not the instance
        px = r * math.cos(theta)
        py = r * math.sin(theta)
        return Point(px, py)

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __repr__(self):
        return f'Point({self.x},{self.y})'

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y
    
    def __neq__(self, p):
        return self.x != p.x or self.y != p.y

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        return None

    def __len__(self):
        return 2

p1 = Point(5, 2) # call the initializer, instantiate the class
p2 = Point(8, 4)
p3 = Point(5, 2)

polar_point = Point.from_polar(5.0, math.pi/6)

class RandomPoint(Point):
    def __helper_function(self):
        new_cord = random.randint(1,10)
        return new_cord

    def __init__(self):
        self.x = self.__helper_function()
        self.y = self.__helper_function()

rp1 = RandomPoint()

print(p1 == p3)
print(p2[0])
print(len(p3))