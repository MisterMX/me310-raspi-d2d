import math
import time

class Circle(object):
    def __init__(self, canvas, x, y, radius, **kwargs):
        self.canvas = canvas
        x1 = x - radius
        x2 = x + radius
        y1 = y - radius
        y2 = y + radius
        self.id = canvas.create_oval(x1, y1, x2, y2, **kwargs)

    def delete(self):
        self.canvas.delete(self.id)

class SonarCircle(object):
    def __init__(self, canvas, x, y, minRadius, **kwargs):
        self.canvas = canvas
        self.kwargs = kwargs
        self.minRadius = minRadius
        self.size = minRadius
        self.id = None
        self.x = x
        self.y = y
        self.lastDrawTime = time.time()
        self.redraw()

    def redraw(self):
        if (self.id is not None):
            self.canvas.delete(self.id)
        
        currentTime = time.time()
        elapsedTime = currentTime - self.lastDrawTime

        x1 = self.x - self.size
        x2 = self.x + self.size
        y1 = self.y - self.size
        y2 = self.y + self.size
        self.id = self.canvas.create_oval(x1, y1, x2, y2, **self.kwargs)

        halfContainerWidth = self.canvas.winfo_width() / 2
        halfContainerHeight = self.canvas.winfo_height() / 2

        if (self.size < math.sqrt(halfContainerWidth * halfContainerWidth + halfContainerHeight * halfContainerHeight)):
            self.size = self.size + 400 * elapsedTime
        else:
            self.size = self.minRadius

        self.lastDrawTime = currentTime
