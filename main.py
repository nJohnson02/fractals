from PIL import Image 
from numpy import complex, array 
import colorsys
import math

print('Input Fractal in terms of z, reals, and c, complex:')
FRACTAL = str(input('z = '))
ITERATIONS = int(input('Iterations: '))
WIDTH, HEIGHT = int(input('Width: ')), int(input('Height: '))
x1, x2 = float(input('Domain Start: ')), float(input('Domain End: '))
y1, y2 = -1*float(input('Range End: ')), -1*float(input('Range Start: '))

A, B = (x2 - x1)/WIDTH, (y2 - y1)/HEIGHT

# return a tuple of colors as rgb values
def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))

def fractal(x, y):
    c = complex(x1+x*A, y1+y*B)
    c = c
    z = 0
    for i in range(1, ITERATIONS):
        if abs(z) > 2: return rgb_conv(i)
        z = eval(FRACTAL) 
    return (0, 0, 0)

img = Image.new('RGB', (WIDTH, HEIGHT))
pixels = img.load()

for x in range(img.size[0]):
    print("%.2f %%" % (x / WIDTH * 100.0))
    for y in range(img.size[1]):
        pixels[x, y] = fractal(x, y)

img.save("sample.png", "")
