#https://people.csail.mit.edu/albert/bluez-intro/c212.html

import bluetooth

#bd_addr = "FC:F8:AE:36:F4:42"
bd_addr = "5C:F3:70:71:A0:B5"
port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("Abel Dean Josh Ben John Shelley Jalen"
          "Abel Dean Josh Ben John Shelley Jalen Abel Dean "
          "Josh Ben John Shelley Jalen Abel Dean"
          "Josh Ben John Shelley Jalen Abel Abel"
          "Dean Josh Ben John Shelley Jalen")


sock.close()