from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0
pensize(2)

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        color(c[0], c[1], c[2])
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)
done()
