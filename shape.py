from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random


class Circle():

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
        drw = ImageDraw.Draw(base,'RGBA')
        coordinate = [(self.x1, self.y1),(self.x2, self.y2)]
        color = (self.red, self.green, self.blue, self.alpha)
        drw.ellipse(coordinate, color, None)
        return base

class Rectangle():

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
        drw = ImageDraw.Draw(base,'RGBA')
        coordinate = [(self.x1, self.y1),(self.x2, self.y2)]
        color = (self.red, self.green, self.blue, self.alpha)
        drw.rectangle(coordinate, color, None)
        return base


class Triangle():

    def __init__(self):
        self.red = random.randint(0,255)
        self.blue = random.randint(0,255)
        self.green = random.randint(0,255)
        self.alpha = random.randint(0,255)
        self.x1 = random.randint(0,400)
        self.y1 = random.randint(0,400)
        self.x2 = random.randint(0,400)
        self.y2 = random.randint(0,400)
        self.x3 = random.randint(0,400)
        self.y3 = random.randint(0,400)

    def draw(self, base):
        #canvas of size 350 * 350
        drw = ImageDraw.Draw(base,'RGBA')
        coordinate = [(self.x1, self.y1),(self.x2, self.y2),(self.x3, self.y3)]
        color = (self.red, self.green, self.blue, self.alpha)
        drw.polygon(coordinate, color, None)
        return base

primitive = [Circle(), Rectangle(), Triangle()]

def Chromosome(select):
    base = Image.new('RGB',(350,350), (255,255,255))
    chromosome = []
    for i in range(100):
        temp = type.__new__(primitive[select])

        chromosome.append(primitive[select])

    for i in range(100):
        base = chromosome[i].draw(base)

    base.show()


def main():
    Chromosome(1)

if __name__ == '__main__':
    main()
