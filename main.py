import imageio
import matplotlib.pyplot as plt
import sys

from Line import Line
from Point import Point

line = Line([])
print("Punkt eingeben (Form: x,y dezimalstellen mit Punkt):")
for stdline in sys.stdin:
    stdline

#line = Line([Point(-3, 9), Point(-2, 4), Point(-1, 1), Point(0, 0), Point(1, 1), Point(2, 4), Point(3, 9)])
#line = Line([Point(0, 3), Point(3, 8), Point(5, 2), Point(8, 5)])
line = Line([Point(0, 0), Point(1, 1), Point(2, 0), Point(3, -1), Point(4, 0)])

bezierLine = Line([])

def createSubLine(line, t):
    newLine = Line([])
    pointLeftOf = None
    for point in line.points:
        if pointLeftOf != None:
            x = point.x - pointLeftOf.x
            y = point.y - pointLeftOf.y

            x *= t / 100
            y *= t / 100

            x += pointLeftOf.x
            y += pointLeftOf.y

            newLine.addPoint(Point(x, y))

        pointLeftOf = point

    plt.plot(newLine.xArray(), newLine.yArray(), '-o')

    if len(newLine.points) > 1:
        createSubLine(newLine, t)
    else:
        bezierLine.addPoint(newLine.points[0])

filenames = []
for t in range(0, 101, 1):
    plt.plot(line.xArray(), line.yArray(), '-o')
    createSubLine(line, t)
    plt.plot(bezierLine.xArray(), bezierLine.yArray())
    plt.savefig("D:\\huhu\\pic" + str(t) + ".png")
    filenames.append("D:\\huhu\\pic" + str(t) + ".png")
    plt.close()



images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('D:\\huhu\\img.gif', images)