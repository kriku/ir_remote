#!/usr/bin/python
import sys, serial, time
from subprocess import call


print(str(sys.argv))

keys = {
    b'E*\xc10\x93\xe5\r\xe1' : "Up",
    b'E*\xc18\xd3\xca\r\xe1' : "Down",
    b'E*\xc1AS\xca\r\xe1': "Left",
    b'E*\xc14\x93\xe5\r\xe1': "Right",
    b'E*\xc11S\xe5\r\xe1': "Return",
    b'E*\xc12"\x19\r\xe1': "1",
    b'E*\xc1A\xaaFC\xe1': "2",
    b'E*\xc16\xcaFC\xe1': "3",
    b'E*\xc11*\x19\r\xe1': "4",
    b'E*\xc19\xb2FC\xe1': "5",
    b'E*\xc15\n\x19\r\xe1': "6",
    b'E*\xc13\x1a\x19\r\xe1': "7",
    b'E*\xc1B\xa2FC\xe1': "8",
    b'E*\xc17\xc2FC\xe1': "9",
    b'E*\xc18\xba7C\xe1': "0",
    b'E*\xc11PTj\n': "BackSpace",
    b'E*\xc1B\x13\x125\n': "Esc",
    b'E*\xc1E\xa6"5\n': "Mod4"
}

while True:
    ser = serial.Serial(str(sys.argv[1]),
                        9600,
                        timeout=0.3,
                        parity=serial.PARITY_EVEN,
                        rtscts=1)
    s = ser.read(100)
    if len(s) == 8:
        key = keys.get(s)
        if key is not None:
            print(key)
            call(["xdotool", "key", key])



# E0E020DF
