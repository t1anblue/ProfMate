from picamera import PiCamera
from time import sleep

def take_picture(camera):
    #camera = PiCamera()
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/ProfMate/pic.jpg')
    camera.stop_preview()
    return



