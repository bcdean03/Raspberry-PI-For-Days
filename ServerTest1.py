#https://people.csail.mit.edu/albert/bluez-intro/c212.html

import bluetooth
import os

os.system("sudo hciconfig hci0 piscan")

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_sock.bind(("FC:F8:AE:36:F4:42",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()
print "Accepted connection from ",address

data = client_sock.recv(1024)
print "received [%s]" % data

client_sock.close()
server_sock.close()