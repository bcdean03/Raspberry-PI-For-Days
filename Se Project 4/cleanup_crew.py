import os
import sys
sys.path.append('/home/pi/Desktop/Se Project 4/Adafruit_PWM_Servo_Driver')
from Adafruit_PWM_Servo_Driver import PWM

RED, GREEN, BLUE = 15,1,14
pw2 = PWM(0x60)
pw2.setPWMFreq(500)
pw2.setAllPWM(0,0)
pw2.setPWM(RED, 0,60)

os.system("echo !!!!RESTARTING!!!!")
#os.system("sudo reboot")

