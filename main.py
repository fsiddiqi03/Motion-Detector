from gpiozero import MotionSensor
from hue_api import hueAPI

hue = hueAPI()
pir = MotionSensor(17)




while True:
    pir.wait_for_motion()
    print("You moved")
    if not hue.lightStatus():
        hue.turnON()
        print('light turned on')
    else:
        print('light already on')





