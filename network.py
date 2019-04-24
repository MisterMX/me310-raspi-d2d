import socket
import threading
import struct
import time

UDP_PORT = 5020
UDP_IP = "0.0.0.0"
UDP_BUFFER_SIZE = 1024

class UdpListener(threading.Thread):
    def __init__(self, onLocationMessageReceived):
        super(UdpListener, self).__init__()
        self.onLocationMessageReceived = onLocationMessageReceived
    
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        while True:
            data = sock.recv(UDP_BUFFER_SIZE)
            [lat,long] = struct.unpack("ff", data)
            self.onLocationMessageReceived({"lat": lat, "long": long})

class UdpSender(threading.Thread):
    def __init__(self):
        super(UdpSender, self).__init__()

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = struct.pack("ff", 30.4, 44.3)
        while True:
            time.sleep(2)
            sock.sendto(message, ("localhost", UDP_PORT))

class NetworkService:
    def __init__(self, onLocationMessageReceived):
        self.onLocationMessageReceived = onLocationMessageReceived
        
    def start(self):
        self._startReceiving()
        self._startSending()

    def _startReceiving(self):
        self.udpListener = UdpListener(self.onLocationMessageReceived)
        self.udpListener.start()

    def _startSending(self):
        self.udpSender = UdpSender()
        self.udpSender.start()
