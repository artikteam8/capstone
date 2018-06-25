rom piCamera import PICamera
from time import sleep
camera = PICamera()
camera.start_preview()
sleep(10)
camera.stop_preview()