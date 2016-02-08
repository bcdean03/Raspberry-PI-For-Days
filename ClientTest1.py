#https://people.csail.mit.edu/albert/bluez-intro/c212.html

import bluetooth

bd_addr = "FC:F8:AE:36:F4:42"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()