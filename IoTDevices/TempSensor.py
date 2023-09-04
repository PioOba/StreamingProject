import random


class TempSensor:
    measureValue = -1
    mean = 25
    sigma = 1
    upTime = -1

    def __init__(self, device_id: int, unitname: str, localization: str, running: bool):
        self.unitName = unitname
        self.running = running
        self.localization = localization
        self.id = device_id

    def turn_on(self):
        self.running = 1

    def turn_off(self):
        self.running = 0

    def generateData(self):
        self.measureValue = random.gauss(self.mean, self.sigma)
