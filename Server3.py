import bluetooth

name="bt_server"
target_name="sigasen"
uuid="00001101-0000-1000-8000-00805F9B34FB"

serverSocket=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
port=bluetooth.PORT_ANY
serverSocket.bind(("",port))
print "Listening for connections on port: ", port
serverSocket.listen(1)
port=serverSocket.getsockname()[1]

#the missing piece
bluetooth.advertise_service( serverSocket, "SampleServer",
               service_id = uuid,
               service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ],
               profiles = [ bluetooth.SERIAL_PORT_PROFILE ]
                )

inputSocket, address=serverSocket.accept()
print "Got connection with" , address
while(True):
    data=inputSocket.recv(1024)
    dataArray = data.split("-")
    print "Degrees:", dataArray[0]
    if dataArray[1] == "f":
        print"Forward:", dataArray[1]
    else:
        print"Backward:", dataArray[1]
    print
    #print type(data)
    #print "received [%s] \n " % data
#inputSocket.send("Hello Abel")
inputSocket.close()
serverSocket.close()