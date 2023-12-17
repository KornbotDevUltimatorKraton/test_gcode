import requests 

read_gcode = open("Catbot3 body_snatcher_right - Solid1.gcode",'r')
read_linecode = read_gcode.readlines()
print(read_linecode)
for gcode in read_linecode:

           print(gcode)
