import imageio
import matplotlib.pyplot as plt
import sys
import os

from Line import Line
from Point import Point
from Progressbar import  Progressbar

line = Line([])
print("Insert points (Form: x,y) continue with \'q\':")
for stdline in sys.stdin:
    if stdline == "q\n" or stdline == "Q\n" or stdline == "quit\n" or stdline == "Quit\n":
        break
    else:
        numbers = stdline.split(",")
        line.addPoint(Point(int(numbers[0]), int(numbers[1])))

print("Define path:")
path = sys.stdin.readline().replace("\n", "")

print("Which resolution do you want (only one number (dpi))")
dpi = sys.stdin.readline().replace("\n", "")
dpi = int(dpi)

# line = Line([Point(-3, 9), Point(-2, 4), Point(-1, 1), Point(0, 0), Point(1, 1), Point(2, 4), Point(3, 9)])
# line = Line([Point(0, 3), Point(3, 8), Point(5, 2), Point(8, 5)])
# line = Line([Point(0, 0), Point(1, 1), Point(2, 0), Point(3, -1), Point(4, 0)])

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
progessbar = Progressbar()
print("calculating...")
for t in range(0, 101, 1):
    plt.plot(line.xArray(), line.yArray(), '-o')
    createSubLine(line, t)
    plt.plot(bezierLine.xArray(), bezierLine.yArray())
    os.makedirs(os.path.normpath(path) + "\\img\\", exist_ok=True)
    plt.savefig(os.path.normpath(path) + "\\img\\" + "pic" + str(t) + ".png", dpi=dpi)
    filenames.append(os.path.normpath(path) + "\\img\\" + "pic" + str(t) + ".png")
    plt.close()

    progessbar.print(t)

print("\ncreate gif...")

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave(os.path.normpath(path) + "\\img.gif", images)

print("done")
