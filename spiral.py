import math
from pystdlib import stddraw as sd

print("spiral")

DIM = 30

IMAGE_SIZE = 1024

sd.setCanvasSize(IMAGE_SIZE, IMAGE_SIZE)

sd.setXscale(-DIM, DIM)
sd.setYscale(-DIM, DIM)

sd.clear(sd.PINK)

x = [0]
y = [0]

POINTS = 1000

delta_alpha = 6 * math.pi / POINTS

for i in range(1, POINTS + 1):
    angle = i * delta_alpha
    x.append(angle * math.cos(angle))
    y.append(angle * math.sin(angle))

    sd.line(x[i - 1], y[i - 1], x[i], y[i])


sd.show()