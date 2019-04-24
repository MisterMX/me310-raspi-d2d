#!/usr/bin/env python3
import tkinter as tk
import time
from view import Circle, SonarCircle
from gps import GpsService
from network import NetworkService

class App(object):
    def __init__(self, master):
        self.master = master
        self._createView()
        self.GpsService = GpsService(lambda val: self.master.after(0, lambda: self._onGpsEvent(val)))
        self.GpsService.start()
        self.NetworkService = NetworkService(lambda msg: self.master.after(0, lambda: self._onNetworkMessage(msg)))
        self.NetworkService.start()
        self.master.after(0, self.animation)

    def _createView(self):
        self.canvas = tk.Canvas(self.master)
        self.canvas.update()
        self.canvas.configure(width = self.master.winfo_width(), height = self.master.winfo_height())
        self.canvas.pack()
        centerX = self.master.winfo_width() / 2
        centerY = self.master.winfo_height() / 2
        self.centerCirlce = Circle(self.canvas, centerX, centerY, 40, fill='red')
        self.sonarCircle = SonarCircle(self.canvas, centerX, centerY, 40, outline='black')

    def _onGpsEvent(self, val):
        print(val)

    def _onNetworkMessage(self, msg):
        print("Network message: ", msg)

    def animation(self):
        self.sonarCircle.redraw()
        self.canvas.pack()
        self.master.after(12, self.animation)

root = tk.Tk()
root.attributes("-fullscreen", True)
container = tk.Frame(root)
container.pack(expand = True, fill = "both")
app = App(container)
root.mainloop()
