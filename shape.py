from PIL import Image, ImageDraw
import numpy as np
import random

COLOR_RANGE = 255

class Parameters:

    @classmethod
    def set(cls, image_size):
        X_Range = image_size[0]
        Y_Range = image_size[1]
        X_Shift = X_Range/10
        Y_Shift = Y_Range/10

class Shape(object):

    def __init__(self):
        
        self.x1 = random.randint(0,Parameters.X_Range)
        self.y1 = random.randint(0,Parameters.Y_Range)
        self.x2 = random.randint(0,Parameters.X_Range)
        self.y2 = random.randint(0,Parameters.Y_Range)

    def draw(self, base):
        global drw
        drw = ImageDraw.Draw(base,'RGBA')
        global coordinate
        coordinate = [(self.x1, self.y1),(self.x2, self.y2)]
        global color
        color = (self.red, self.green, self.blue, self.alpha)

    def remake(self):
        self.x1 = self.x1 + random.randint(-1*Parameters.X_Shift,Parameters.X_Shift)
        self.x2 = self.x2 + random.randint(-1*Parameters.X_Shift,Parameters.X_Shift)
        self.y1 = self.y1 + random.randint(-1*Parameters.Y_Shift,Parameters.Y_Shift)
        self.y2 = self.y2 + random.randint(-1*Parameters.Y_Shift,Parameters.Y_Shift)

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
        super().draw(base)
        drw.rectangle(coordinate, color, None)
        return base

    def remake(self):
        super().remake()


class Triangle(Shape):

    def __init__(self):
        super().__init__()
        self.x3 = random.randint(0,Parameters.X_Range)
        self.y3 = random.randint(0,Parameters.Y_Range)

    def draw(self, base):
        super().draw(base)
        coordinate.append((self.x3, self.y3))
        drw.polygon(coordinate, color, None)
        return base

    def remake(self):
        super().remake()
        self.x3 = self.x3 + random.randint(-1*Parameters.X_Shift,Parameters.X_Shift)
        self.y3 = self.y3 + random.randint(-1*Parameters.Y_Shift,Parameters.Y_Shift)


primitive = [Circle(), Rectangle(), Triangle()]
