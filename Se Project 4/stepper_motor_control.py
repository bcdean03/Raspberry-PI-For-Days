#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)


myStepper = mh.getStepper(200, 1)  	# 200 steps/rev, motor port #1
myStepper.setSpeed(30)  		# 30 RPM

def degree_to_steps(deg):
	return int((int(deg)/1.8))

def move_motor_F_or_B(fOrb, deg):
	if(fOrb == 'f'):
		myStepper.step(degree_to_steps(deg), Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
	else:
		myStepper.step(degree_to_steps(deg), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)









