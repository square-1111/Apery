from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random

#class ShapeList(enum.Enum):



class Circle():

    def __init__(self):
        self.color = (random.randint(0,255),random.randint(0,255), random.randint(0,255), random.randint(0,250))
        self.x1 = random.randint(0,400)
        self.y1 = random.randint(0,400)
        self.x2 = random.randint(0,400)
        self.y2 = random.randint(0,400)
  
    def draw(self, base):
        txt = Image.new('RGBA',(350,350), (0,0,0,0))
        d = ImageDraw.Draw(txt)
        d.ellipse([(self.x1,self.y1),(self.x2,self.y2)], fill=self.color)
        base = Image.alpha_composite(base,txt)
        #self.calculate_fitness()
        return base

    #def calculate_fitness():
        

def main():
    #original = Image.open('mona_orig.jpg')
    base = Image.new('RGBA',(350,350), (0,0,0,0))
    genes = []
    for i in range(100):
        temp = Circle()
        genes.append(temp)

    for i in range(100):
        base = genes[i].draw(base)

    base.save('cir.png')

if __name__ == '__main__':
    main()
        
