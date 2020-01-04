from PIL import Image 
from numpy import complex, array 
import colorsys
import math

print('Input Fractal in terms of z, reals, and c, complex:')

# Fractal basic info
FRACTAL = str(input('z = '))
ITERATIONS = int(input('Iterations: '))
WIDTH, HEIGHT = int(input('Width: ')), int(input('Height: '))

# Domain input
x1, x2 = float(input('Domain Start: ')), float(input('Domain End: '))
y1, y2 = -1 * float(input('Range Start: ')), -1 * float(input('Range End: '))
A, B = (x2 - x1) / WIDTH, (y2 - y1) / HEIGHT

# Grid
GRID = str(input('Display Grid (y/n): '))
NUM, GWIDTH, GHEIGHT = 1, 1, 1

if GRID == 'y':
    NUM = int(input('Grid Size: '))
    GWIDTH, GHEIGHT = WIDTH / NUM, HEIGHT / NUM

# Color converter
def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))

#Fractal Generator
def fractal(x, y):

    z, c = 0, complex(x1+x*A, y1+y*B)
    c = c

    if (x%(GWIDTH) > 0.75 or x%(GWIDTH) < -0.75) and (y%(GHEIGHT) > 0.75 or y%(GHEIGHT) < -0.75) and (y != (HEIGHT)-1) and (x != (WIDTH)-1) or (GRID == 'n'):

        for i in range(1, ITERATIONS):
            if abs(z) > 2: return rgb_conv(i)
            z = eval(FRACTAL)

        return (0, 0, 0)

    else: return (200, 200, 200)

img = Image.new('RGB', (WIDTH, HEIGHT))
pixels = img.load()

# Image generator
for x in range(img.size[0]):
    print("%.2f %%" % (x / WIDTH * 100.0))
    for y in range(img.size[1]): pixels[x, y] = fractal(x, y)

img.save("sample.png", "")

# Text Output
y1, y2 = -y1, -y2
f = open('sample.txt', 'w')
f.write("Fractal: z = " + FRACTAL + '\n')
f.write("Resolution: " + str(WIDTH) + 'x' + str(HEIGHT) + '\n')
f.write("Domain: [{}, {}]\n".format(str(x1), str(x2)))
f.write("Range: [{}, {}]\n".format(str(y1), str(y2)))

if GRID == 'y':
    f.write("Grid Width: {}\n".format(str((x2-x1)/NUM)))
    f.write("Grid Height: {}\n".format(str((y2-y1)/NUM)))

f.close()