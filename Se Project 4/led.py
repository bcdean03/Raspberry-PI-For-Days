from threading import Thread
import sys
#sys.path.insert(0,'/home/pi/Desktop/Se Project 4/Adafruit_PWM_Servo_Driver')
sys.path.append('/home/pi/Desktop/Se Project 4/Adafruit_PWM_Servo_Driver')
from Adafruit_PWM_Servo_Driver import PWM
import time
import led_attribute
class LED_T(Thread):

	def __init__(self, f, name="LED"):
		Thread.__init__(self, name=name)
		self.RED, self.GREEN, self.BLUE = 15,1,14
		self.pw2 = PWM(0x60)
		#self.freq = f
		#self.pw2.setPWMFreq(self.freq)
		self.previous = led_attribute.state

	def run(self):
		while(True):
			if((led_attribute.state == led_attribute.RED_BLINKING or
 			     led_attribute.state == led_attribute.GREEN_BLINKING or 
			     led_attribute.state == led_attribute.BLUE_BLINKING)):
				self.blink_LED()
			else: 
				break


	def blink_LED(self):
		if(led_attribute.state == led_attribute.RED_BLINKING):
			self.turn_off_blue_green_led()
			self.pw2.setPWM(self.RED,0,600)
			time.sleep(.5)
			self.pw2.setPWM(self.RED,0,0)
			time.sleep(.1)
		elif(led_attribute.state == led_attribute.GREEN_BLINKING):
			self.turn_off_red_blue_led()
			self.pw2.setPWM(self.GREEN,0,600)
			time.sleep(.5)
			self.pw2.setPWM(self.GREEN,0,0)
			time.sleep(.1)
		elif(led_attribute.state == led_attribute.BLUE_BLINKING):
			self.turn_off_red_green_led()
			self.pw2.setPWM(self.BLUE,0,600)
			time.sleep(.5)
			self.pw2.setPWM(self.BLUE,0,0)
			time.sleep(.1)

	def turn_off_red_green_led(self):
		self.pw2.setPWM(self.GREEN,0,0)
		self.pw2.setPWM(self.RED,0,0)

	def turn_off_red_blue_led(self):
		self.pw2.setPWM(self.RED,0,0)
		self.pw2.setPWM(self.BLUE,0,0)

	def turn_off_blue_green_led(self):
		self.pw2.setPWM(self.GREEN,0,0)
		self.pw2.setPWM(self.BLUE,0,0)
	










