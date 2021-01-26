import usb.core

VID = 0x045e
PID = 0x02ea

dev = usb.core.find(idVendor=VID, idProduct=PID)

if not dev:
    raise ValueError('Device not found')
else:
    print(dev)
    # dev.set_configuration()

dev.read(0x81,100000,1000)