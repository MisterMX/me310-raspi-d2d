import threading
import time

class GpsService(threading.Thread):
    def __init__(self, onLocationChangedHandler):
        super(GpsService, self).__init__()
        self.onLocationChangedHandler = onLocationChangedHandler

    def run(self):
        while True:
            time.sleep(1)
            newLocation = {"lat": 40.0, "long": 30.0}
            self.onLocationChangedHandler(newLocation)
