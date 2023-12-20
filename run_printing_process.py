import re
import time 
import json 
import requests 

read_gcode = open("benchy.gcode",'r')
read_linecode = read_gcode.readlines()
#print(read_linecode)

current_command = {}
position_processing = {}  
total_layer = len(read_linecode)
print_layer = [] 
internal_pos = {} # Get the internal position data 
step_data = {"step":0.1} # Get the step to calculate the position data containing in the system 

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
           #print(read_linecode[gcode],len(read_linecode[gcode].split(";")),percentage)
           #print(read_linecode[gcode].split(";")[0])
           #Check if the line of the code is consist of the data 
           #time.sleep(0.1)
           gcode_container = read_linecode[gcode].split(";")[0] 
           if gcode_container != " ": 
                    print(gcode_container)
                    #Convert g-code into the json data
                    split_check = gcode_container.split(" ") 
                    #print(split_check)
                    remove_comment = ["Printing...\n"] # Check if the second element in the array is not in this list 
                    if len(split_check) >= 2:
                            if split_check[1] == '': 
                                        print("single command parameter ")    
                                        print(split_check) 
                                        current_command["command"] = split_check[0]
                                        element_pos = split_string(split_check[0]) 
                                        print(element_pos)
                                    
                                        internal_pos[element_pos[0]] = element_pos[1]
                                        print(internal_pos)
                                        position_processing[current_command["command"]] = internal_pos  # Get the 
                                        #Sending the post request data here 
                                        print(position_processing)
                                        internal_pos.clear()
                                        position_processing.clear()

                            if split_check[1] != '' and split_check not in remove_comment:
                                        #Multiple parameters data 
                                        print("Multiple position command")
                                        print(split_check) # The position data manipulators can be re calculate as the 
                                        current_command["command"] = split_check[0]
                                        for gread in range(1,len(split_check)):
                                               #if split_check[len(split_check)-1]  != '':  
                                               element_pos = split_string(split_check[gread])
                                               print(element_pos)
                                               #if element_pos != []:
                                               #      internal_pos[element_pos[0]] = element_pos[1]
                                               #      print(internal_pos)
                                               '''
                                                     if len(split_check[gread])-1 == gread:
                                                          position_processing[current_command["command"]] = internal_pos
                                                          #Sending the post request data here 
                                                          print(position_processing) 
                                                          internal_pos.clear()
                                                          position_processing.clear() 
                                               '''

                                       
                                 
                  
           '''
           if  len(read_linecode[gcode].split(";")) == 2:
                   if read_linecode[gcode].split(";")[0] == '':    
                       pass
                       #print("Comment detected",read_linecode[gcode].split(";"))
           else:
               print("Command detected",read_linecode[gcode].split(" ")) 
               #Running the command header extraction for the G-code and calibrate the position data into the json configuretion 
               #Detect_comment and command 
               current_command["command"] = read_linecode[gcode].split(" ")[0]
               #gcode.split(" ").remove(gcode.split(" ")[0]) # Remove the first element of the data in the list 
           '''    
               #if len(read_linecode[gcode]) > 1:
           '''
               for gread in range(1,len(read_linecode[gcode].split(" "))):
                         print(gread)   # Get the data of the gread from the current data 
                         result_split = split_string(read_linecode[gcode].split(" ")[gread])
                           #Detect the interception between the data 
                         if len(result_split) == 2:  
                           try:    
                              internal_pos[result_split[0]] = result_split[1] 
                              print(internal_pos)
                           except:
                                pass                
                           if len(read_linecode[gcode].split(" "))-1 == gread:
                                          data_post = {current_command["command"]:internal_pos} #Send the data of the position in the realtime  
                                          print("Position command",data_post) 
                                          #Post request data here with full command 
                                          internal_pos.clear()
     
                           #internal_pos.clear() # Clear and get the new one to send the post request                            
               
               '''   
                  
