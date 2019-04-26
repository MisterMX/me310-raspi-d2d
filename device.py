import uuid 

def getDeviceId():
    return uuid.getnode()

def isThisDevice(deviceId):
    thisDeviceId = getDeviceId()
    return deviceId == thisDeviceId
