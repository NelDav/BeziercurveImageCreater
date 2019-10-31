from Point import Point
import numpy as np
import matplotlib.pyplot as plt

class Line:
    points = []

    def __init__(self, points):
        self.points = points

    def addPoint(self, point):
        self.points.append(point)

    def draw(self):
        plt.plot(self.xArray(), self.yArray(), '-o')
        plt.show()

    def xArray(self):
        result = []
        for point in self.points:
            result.append(point.x)

        return result

    def yArray(self):
        result = []
        for point in self.points:
            result.append(point.y)

        return result
