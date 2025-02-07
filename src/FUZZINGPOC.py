#!/usr/bin/env python3
          

import sys
import os
import time
from bs4 import BeautifulSoup
from typing import final
#Abstraction.
#Store Stuff.
i = 0
result = 0 #Keeping assert statement to use it again :)
assert result >= 0, "Never input negatives."

reminder = "this is just a POC, originally this was made to BrutForce HOST ID's via an AD Config File (Samba User Enumeration)"
reminder2 = "NOTE TO FUTURE SELF: "

number_fuzz = None
class Fuzzer(): 
    
    def __init__(self):
        pass

    @final #Dont touch my shit :D 
    def get_details():
        return sys.platform
    
    def send_command(self,range_end,counter): #Without Looping, create a one time function, could also do a Recursion untill limit is reached tho.
        
        try:
            if range_end == counter:
                sys.exit()
                
            host_brutforce ="Hazard S-1-5-21-4254423774-1266059056-3197185112-" #Changed to Ping, for POC.
            
            fuzzed_part = number_fuzz + counter + 1
            fuzzed_part = str(fuzzed_part)
            enum = host_brutforce + fuzzed_part 
            os.system(enum)
            time.sleep(0.5)
                
            self.send_command(range_end,counter=counter+1)
            
        except KeyboardInterrupt:
            print(" EXITING")
            sys.exit()
    

def output_function(self):
    print(self.get_details())
