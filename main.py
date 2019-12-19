from PIL import Image 
from numpy import complex, array 
import colorsys
import math

print('Input Fractal in terms of z, reals, and c, complex:')
FRACTAL = str(input('z = '))
ITERATIONS = int(input('Iterations: '))
WIDTH = int(input('Width: '))
HEIGHT = int(input('Height: '))
x1 = float(input('Domain Start: '))
x2 = float(input('Domain End: '))
y2 = -1*float(input('Range Start: '))
y1 = -1*float(input('Range End: '))

A = (x2 - x1)/WIDTH
B = (y2 - y1)/HEIGHT
# a function to return a tuple of colors 
# as integer value of rgb 
def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))

# function defining a fractal
def fractal(x, y):
    c = complex(x1+x*A, y1+y*B)
    c = c
    z = 0
    for i in range(1, ITERATIONS):
        if abs(z) > 2:
            return rgb_conv(i)
        #Fractal Algorithm
        z = eval(FRACTAL)
        #----------------
    return (0, 0, 0)

# creating the new image in RGB mode 
img = Image.new('RGB', (WIDTH, HEIGHT))
pixels = img.load()

for x in range(img.size[0]):
    print("%.2f %%" % (x / WIDTH * 100.0))
    for y in range(img.size[1]):
        pixels[x, y] = fractal(x, y)
       
       # pixels[x, y] = fractal( (x - (0.75 * WIDTH)) / (WIDTH / 4), (y - (WIDTH / 4)) / (WIDTH / 4) )
  
# to display the created fractal after
# completing the given number of iterations
img.save("sample.png", "")
