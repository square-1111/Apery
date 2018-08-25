from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random

class Shape(object):
    # def __new__(cls, *args, **kwargs):
    #             #print "Creating Instance"
    #     instance = super()(Circle, cls).__new__(cls, *args, **kwargs)
    #     return instance


    def __init__(self):
        self.red = random.randint(0,255)
        self.blue = random.randint(0,255)
        self.green = random.randint(0,255)
        self.alpha = random.randint(0,255)
        self.x1 = random.randint(0,400)
        self.y1 = random.randint(0,400)
        self.x2 = random.randint(0,400)
        self.y2 = random.randint(0,400)

    def draw(self, base):
        #canvas of size 350 * 350
        global drw
        drw = ImageDraw.Draw(base,'RGBA')
        global coordinate
        coordinate = [(self.x1, self.y1),(self.x2, self.y2)]
        global color
        color = (self.red, self.green, self.blue, self.alpha)

    def remake(self):
        x,y,z = random.sample(range(-50,50),3)
        self.red = self.red + x
        self.blue = self.blue + y
        self.green = self.green + z
        self.alpha = random.randint(0,255)

class Circle(Shape):

    def __init__(self):
        super().__init__()

    def draw(self, base):
        super().draw(base)
        drw.ellipse(coordinate, color, None)
        return base

    def remake(self):
        super().remake()

class Rectangle(Shape):

    def __init__(self):
        super().__init__()

    def draw(self, base):
        #canvas of size 350 * 350
        super().draw(base)
        drw.rectangle(coordinate, color, None)
        return base

    def remake(self):
        super().remake()


class Triangle(Shape):

    def __init__(self):
        super().__init__()
        self.x3 = random.randint(0,400)
        self.y3 = random.randint(0,400)

    def draw(self, base):
        super().draw(base)
        coordinate.append((self.x3, self.y3))
        drw.polygon(coordinate, color, None)
        return base

    def remake(self):
        super().remake()

primitive = [Circle(), Rectangle(), Triangle()]
