import socket
import threading
import struct
import time
import device

UDP_PORT = 5020
UDP_IP = "0.0.0.0"
UDP_BUFFER_SIZE = 1024

class UdpListener(threading.Thread):
    def __init__(self, onLocationMessageReceived):
        super(UdpListener, self).__init__()
        self._stop_event = threading.Event()
        self.onLocationMessageReceived = onLocationMessageReceived
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        while not self.stopped():
            data = sock.recv(UDP_BUFFER_SIZE)
            [deviceId, lat,long] = struct.unpack("iff", data)
            self.onLocationMessageReceived({"deviceId": deviceId, "lat": lat, "long": long})

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

class UdpSender(threading.Thread):
    def __init__(self):
        super(UdpSender, self).__init__()

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = struct.pack("ff", 30.4, 44.3)
        while not self.stopped():
            time.sleep(2)
            sock.sendto(message, ("localhost", UDP_PORT))

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

class NetworkService:
    def __init__(self, onLocationMessageReceived):
        self.onLocationMessageReceived = onLocationMessageReceived
        self.deviceId = device.getDeviceId()

    def start(self):
        self._startReceiving()
        # self._startSending()

    def _startReceiving(self):
        self.udpListener = UdpListener(self.onLocationMessageReceived)
        self.udpListener.start()

    def stop(self):
        self.udpListener.stop()
        # self.udpSender.stop()

    # def _startSending(self):
        # self.udpSender = UdpSender()
        # self.udpSender.start()

    def broadcastPosition(self, position):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = struct.pack("lff", self.deviceId, position["lat"], position["long"])
        sock.sendto(message, ("localhost", UDP_PORT))
