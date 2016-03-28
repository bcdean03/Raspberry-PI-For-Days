#from Adafruit_PWM_Servo_Driver1.Adafruit_PWM_Servo_Driver import PWM
import sys
#sys.path.insert(0,'/home/pi/Desktop/Se Project 4/Adafruit_PWM_Servo_Driver')
sys.path.append('/home/pi/Desktop/Se Project 4/Adafruit_PWM_Servo_Driver')
from Adafruit_PWM_Servo_Driver import PWM
import time
import led_attribute

'''
print(moduleTest.bool)
moduleTest.bool = True
print(moduleTest.bool)
'''
RED, GREEN, BLUE = 15,1,14
pw = PWM(0x60)
pw.setPWMFreq(400)
pw.setAllPWM(0,0)

while(True):
	pw.setPWM(GREEN, 0,4095)
	time.sleep(.5)
	pw.setAllPWM(0,0)
	time.sleep(.1)

pw.setPWMFreq(400)
pw.setAllPWM(0,0)
#pw.setPWM(RED, 0,4095)
#pw.setPWM(GREEN, 0,4095)
#pw.setAllPWM(40,100)
#pw.setPWMFreq(4)
#pw.setPWM(14,0,600)

'''
for i in xrange(1,1000,10):
	pw = PWM(0x60)
	pw.setAllPWM(0,0)
	pw.setPWMFreq(4)
	pw.setPWM(14,0,i)
	#pw.setAllPWM(0,0)
	print("i:",i)
	time.sleep(2)

pw = PWM(0x60)
pw.setAllPWM(0,0)
pw.setPWMFreq(500)
pw.setPWM(14,0,600)
'''

'''
led = LED_T()
led.start()
led_attribute.state = led_attribute.RED_SOLID
time.sleep(5)
led_attribute.state = led_attribute.GREEN_SOLID
time.sleep(5)
led_attribute.state = led_attribute.BLUE_SOLID
time.sleep(5)
led_attribute.state = led_attribute.RED_BLINKING
time.sleep(5)
led_attribute.state = led_attribute.GREEN_BLINKING
time.sleep(5)
led_attribute.state = led_attribute.BLUE_BLINKING
time.sleep(5)
led_attribute.state = led_attribute.TURN_OFF
print("OUTAHH")
'''

'''pw = PWM(0x60)
pw.setPWMFreq(500)
pw.setPWM(15,1024,3072)
'''
#pw2 = PWM(0x60)
#freq is 40 - 1000
#pw2.setPWMFreq(0)
#pw2.setPWM(15, 1024, 3072)

#0-15 for channels the first parameter in setPWM
#0-4095 are the ranges of the next two parameters of setPWM
#for i in range(0,15):
#	print("i:", i)
#	pw2.setPWM(i,1024,3072)
#	time.sleep(1)

#pw2.setPWM(15,1024,1)


#pw2.setPWM(1,15,0)
#time.sleep(5)
#pw2.setPWM(14,400,0)
#time.sleep(5)
# off - parameter 1(0v), on - parameter 2 (5v)
#pw2.setPWM(15,3500,4000)
#time.sleep(5)
'''
pw2.setPWMFreq(0)

#RED, GREEN, BLUE = 15,1,14
pw2.setPWM(14,0,0)
pw2.setPWM(15,0,100)
pw2.setPWM(1,0,200)
'''
'''
time.sleep(5)
pw2.setPWM(15,0,0)
pw2.setPWM(14,0,0)
pw2.setPWM(1,0,0)
pw2.setPWM(15,10,200)
pw2.setPWM(14,10,200)
pw2.setPWM(1,10,200)
'''
	
'''
pw2.setPWMFreq(500)
while(True):
	pw2.setPWM(15,5,4000)
	time.sleep(1)
	pw2.setPWM(15,0,0)
	pw2.setPWM(14,5,4000)
	time.sleep(1)
	pw2.setPWM(14,0,0)
	pw2.setPWM(1,5,4000)
	time.sleep(1)
	pw2.setPWM(1,0,0)
	break
pw2.setPWMFreq(0)

pw2.setPWM(1,5,1000)
time.sleep(2)
pw2.setPWM(1,0,0)
time.sleep(2)
pw2.setPWM(14,5,1000)
time.sleep(2)
pw2.setPWM(14,0,0)
time.sleep(2)
pw2.setPWM(15,5,1000)
time.sleep(2)
pw2.setPWM(15,0,0)
time.sleep(2)
'''

#for i in range(0,16):
#	print("i:", i)
#	pw2.setPWM(i,1500,000)
#	time.sleep(2)