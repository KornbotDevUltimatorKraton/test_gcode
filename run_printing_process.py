import time 
import json 
import requests 

read_gcode = open("Catbot3 body_snatcher_right - Solid1.gcode",'r')
read_linecode = read_gcode.readlines()
#print(read_linecode)

current_command = {}
position_processing = {}  
total_layer = len(read_linecode)
print_layer = [] 
for gcode in read_linecode:

           #print(gcode.split(" "))
           print_layer.append(gcode.split(" "))
           percentage = (len(print_layer)/total_layer)*100          
           #res_print = requests.post("http://192.168.50.139:8000/gauge_value",json={"percentage":percentage})  
           #Check the data type of command and comment 
           if  len(gcode.split(";")) == 2:
                   if gcode.split(";")[0] == '':    
                       pass
                       #print("Comment detected",gcode.split(";"))
           else:
               print("Command detected",gcode.split(" "))    
               #Running the command header extraction for the G-code and calibrate the position data into the json configuretion 
               #for gread in gcode.split(" "):
                          #print(gread[0])
               current_command["command_head"] = gcode.split(" ")[0]
               print(current_command)   
               for gread in gcode.split(" "):
                          #Check if position parameter inside is not inside the loop then do the intersection and cut key and value out from the dict 
                          print("running the parameter inside command loop data")
                          
                      
                      
