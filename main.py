from IoTDevices.TempSensor import TempSensor as TempSensor
from time import sleep
if __name__ == "__main__":
    # "Run" sensors:
    Ts1 = TempSensor(device_id=1, unitname='PL1', localization='Warsaw', running=True)
    Ts2 = TempSensor(device_id=2, unitname='PL2', localization='Cracov', running=True)
    Ts3 = TempSensor(device_id=3, unitname='PL3', localization='Poznan', running=True)

    # Generate data
    while True:
        Ts1.generateData()
        print("Ts1:", Ts1.measureValue)

        Ts2.generateData()
        print("Ts2:", Ts2.measureValue)

        Ts3.generateData()
        print("Ts3:", Ts3.measureValue)

        sleep(2)


