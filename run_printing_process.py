import re
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
internal_pos = {} # Get the internal position data 

#stringand_number_dector
def split_string(s):
           parts = re.findall(r'([a-zA-Z]+|\d+)',s)
           return parts
 
#for gcode in read_linecode:
for gcode in range(0,len(read_linecode)):
           #print(gcode.split(" "))
           print_layer.append(read_linecode[gcode].split(" "))
           percentage = (len(print_layer)/total_layer)*100          
           #res_print = requests.post("http://192.168.50.139:8000/gauge_value",json={"percentage":percentage})  
           #Check the data type of command and comment 
           if  len(read_linecode[gcode].split(";")) == 2:
                   if read_linecode[gcode].split(";")[0] == '':    
                       pass
                       #print("Comment detected",gcode.split(";"))
           else:
               print("Command detected",read_linecode[gcode].split(" ")) 
               #Running the command header extraction for the G-code and calibrate the position data into the json configuretion 
               #Detect_comment and command 
               current_command["command"] = read_linecode[gcode].split(" ")[0]
               #gcode.split(" ").remove(gcode.split(" ")[0]) # Remove the first element of the data in the list 
               for gread in range(1,len(read_linecode[gcode].split(" "))):
                           print(gread)   # Get the data of the gread from the current data 
                           result_split = split_string(read_linecode[gcode].split(" ")[gread])
                           #Detect the interception between the data 
                           try:
                              internal_pos[result_split[0]] = result_split[1] 
                              print(internal_pos)
                              
                              if len(gcode.split(" "))-1 == gread:
                                          data_post = {current_command["command"]:internal_pos} #Send the data of the position in the realtime  
                                          print("Position command",data_post) 
                                          #Post request data here with full command 
                                          internal_pos.clear()
                           except:
                                print("Out of range command running the command separately") 
                           #internal_pos.clear() # Clear and get the new one to send the post request                            
               
                  
                  
