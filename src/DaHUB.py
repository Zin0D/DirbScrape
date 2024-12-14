#!/usr/bin/env python3
          
""" DISCLAIMER """
""" DOWNLOAD TOOL IN OPT, MAKE SURE TO BE OWNER OF OPT && give SCRIPT PERMISSIONS """ 

import sys
import CMWebScraper
import BrutForceDirToParse
import FUZZINGPOC
from typing import final 
#Abstraction.
#Store Stuff.

Art =r""" 
                      __    
(\,------------------'()'--o
 (_    _BRUTFORCING_    /~" 
  (_)_)            (_)_)     
    """

Art2 =r""" 
                      __    
(\,------------------'()'--o
 (_    _SCRAPING IT_    /~" 
  (_)_)            (_)_)     
    """

    

def output_function(self):
    print(self.get_details())

if __name__ == "__main__":
    CMWebScraper.CleanFiles()
    print(r"""
 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀ ██░ ██  █    ██  ▄▄▄▄   
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██░ ██▒ ██  ▓██▒▓█████▄ 
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▀▀██░▓██  ▒██░▒██▒ ▄██
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░▓█ ░██ ▓▓█  ░██░▒██░█▀  
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▓█▒░██▓▒▒█████▓ ░▓█  ▀█▓
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒ ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░▒▓███▀▒
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ▒ ░▒░ ░░░▒░ ░ ░ ▒░▒   ░ 
 ░  ░░ ░  ░   ▒   ░        ░ ░░ ░  ░  ░░ ░ ░░░ ░ ░  ░    ░ 
 ░  ░  ░      ░  ░░ ░      ░  ░    ░  ░  ░   ░      ░      
                  ░                                      ░ 
        """)
    try:
        print("NOW ALSO WITH TOR TRAFFIC!")
        SELECTION = int(input("What shall be done\nFUZZ-SomeStuff[1],\nWEB-Scraping[2]\nDIR-BrutForce[3]\nSSH-BrutForce[4]\n: "))
    except KeyboardInterrupt:
        print("Quiting...")
        sys.exit()

    match SELECTION:

        case 1:
            try:
                end = int(input("Input Start Host-ID Section () _."))
                FUZZINGPOC.number_fuzz = end
                print(FUZZINGPOC.Fuzzer().send_command(int(input("Input Range to END")),0))
                
            except Exception as e:
                print(f"Something went wrong: _{e}_")
                sys.exit()
        
        case 2:
            print(Art)
            BrutForceDirToParse.clean_files()
            BrutForceDirToParse.start_threads()
            BrutForceDirToParse.host_list() 
            CMWebScraper.WebScraper.web_scraping()
            print(Art2)
            for x in CMWebScraper.WebScraper.anchor_filter(): #Uncomment to get Sorted List.
                print(x)
            BrutForceDirToParse.clean_files()
            

        case 3:
            words = BrutForceDirToParse.get_words()
            BrutForceDirToParse.brutforcer(words=words)

        case 4:
            host = input("Enter the host: ")
            username = input("Enter the username: ")
            attempts = 0
            CMWebScraper.brut_force_function(host, username, attempts)
        
        case _:
            print("Exiting")
            sys.exit()