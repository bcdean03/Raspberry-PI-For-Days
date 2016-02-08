import bluetooth

target_name = "Dean Bailey (SM-T230NU"
target_address = "34:BE:00:74:6D:11"

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    #print("Address: " + bdaddr)
    #print(bluetooth.lookup_name( bdaddr ))
    if target_name == bluetooth.lookup_name( bdaddr ) and target_address == bdaddr:
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with \naddress:", target_address, "\nname:", target_name
else:
    print "could not find target bluetooth device nearby"