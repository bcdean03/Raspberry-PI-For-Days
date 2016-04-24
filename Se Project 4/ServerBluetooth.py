import os
import bluetooth
import sys
sys.path.append('/home/pi/Desktop/Se Project 4/Adafruit_PWM_Servo_Driver')
from Adafruit_PWM_Servo_Driver import PWM
import led_attribute #This is the one instance module for changing LED status
from led import LED_T
import stepper_motor_control as stepper
import time

RED, GREEN, BLUE = 15,1,14
pw2 = PWM(0x60)
pw2.setPWMFreq(500)

def set_frequency_blinking(color):
	pw2.setAllPWM(0,0)
	led_attribute.state = color
	LED_T(500).start()
	

def set_frequency_solid(color):
	pw2.setAllPWM(0,0)
	time.sleep(.05)
	led_attribute.state = color
	pw2.setPWM(color, 0, 600)


os.system("sudo hciconfig hc0 piscan")
uuid="00001101-0000-1000-8000-00805F9B34FB"
serverSocket=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
port=bluetooth.PORT_ANY
serverSocket.bind(("",port))

set_frequency_blinking(led_attribute.BLUE_BLINKING)


print "Listening for connections on port: ", port
serverSocket.listen(1)

#the missing piece
bluetooth.advertise_service( serverSocket, "SampleServer",
               service_id = uuid,
               service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ],
               profiles = [ bluetooth.SERIAL_PORT_PROFILE ]
                )


while(True):
	print("Waiting for connection...")
	inputSocket, address=serverSocket.accept()
	print "Got connection with" , address
	set_frequency_solid(BLUE)

	while(True):
		try:
			data=inputSocket.recv(1024)

			set_frequency_solid(GREEN)

			#TODO -> Maybe going to check if they sent "Quit"
			print("data:",data)
			data_array = data.split("-")
			stepper.move_motor_F_or_B(data_array[1], int(data_array[0]))
		except:
			set_frequency_blinking(led_attribute.GREEN_BLINKING)

			print("Lost Connection")
			break
			
set_frequency_blinking(led_attribute.RED_BLINKING)

inputSocket.close()
serverSocket.close()
