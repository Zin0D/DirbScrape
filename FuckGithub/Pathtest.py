#!/usr/bin/env python3

import argparse
import socket
import sys
import threading
import subprocess
import os
#Enviroment Variables
Powershell = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"

#There are some Commands you want to seperate via ";"
#seperating via ; , is like using the && Operation (for Powershell ;)

def execute_test(comands):
 
    result_execute = subprocess.run(comands, 
                        capture_output=True, 
                        text=True, shell=True, 
                        executable=Powershell)
    print(result_execute.stdout)

def execute():  
    extension = input("Input what file extension to search for.") 
    file_extension = extension
    
    os.chdir('C:\\')
    Search = f"ls -recurse -ErrorAction SilentlyContinue | where {{($_.name -like '*.{ file_extension}')}}"  
    result = subprocess.run(Search, 
                        capture_output=True, 
                        text=True, shell=True, 
                        executable=Powershell)
    print(result.stdout)

def return_path(path):
    if os.path.exists(path):
        content = os.listdir(path)
        for i in content:
            print(i)
    else:
        print("Path-Does-Not-Exist.")

print(f"Printing Current Working-Directory:[{os.getcwd()}]\n\n")

execute()
return_path("C:\\")
print(bin(9)) #Returns number in Binary ;D

if __name__ == '__main__':
    pass