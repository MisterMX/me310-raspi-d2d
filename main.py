#!/usr/bin/env python3
import tkinter as tk
import time
import math

# class Alien(object):
#     def __init__(self, canvas, *args, **kwargs):
#         self.canvas = canvas
#         self.id = canvas.create_oval(*args, **kwargs)
#         self.vx = 5
#         self.vy = 0

#     def move(self):
#         x1, y1, x2, y2 = self.canvas.bbox(self.id)
#         if x2 > 400:
#             self.vx = -5
#         if x1 < 0:
#             self.vx = 5
#         self.canvas.move(self.id, self.vx, self.vy)

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

class App(object):
    def __init__(self, master, **kwargs):
        self.master = master
        self.canvas = tk.Canvas(self.master)
        self.canvas.update()
        self.canvas.configure(width = master.winfo_width(), height = master.winfo_height())
        self.canvas.pack()
        # self.aliens = [
        #     Alien(self.canvas, 20, 260, 120, 360,
        #           outline='white', fill='blue'),
        #     Alien(self.canvas, 2, 2, 40, 40, outline='white', fill='red'),
        # ]
        centerX = master.winfo_width() / 2
        centerY = master.winfo_height() / 2
        self.centerCirlce = Circle(self.canvas, centerX, centerY, 40, fill='red')
        self.sonarCircle = SonarCircle(self.canvas, centerX, centerY, 40, outline='black')
        # self.canvas.pack()
        self.master.after(0, self.animation)

    def animation(self):
        # for alien in self.aliens:
        #     alien.move()
        self.sonarCircle.redraw()
        self.canvas.pack()
        self.master.after(12, self.animation)

root = tk.Tk()
root.attributes("-fullscreen", True)
container = tk.Frame(root)
container.pack(expand = True, fill = "both")
app = App(container)
root.mainloop()
