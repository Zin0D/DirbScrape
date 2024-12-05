#!/usr/bin/env python3

import threading 
import socket
import sys
from datetime import datetime
import time

#Scann da Port
def ProbeVersion(target,port):
    try:
        probe_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        probe_socket.setblocking(True)
        probe_socket.settimeout(4)
        if True:
            try:
                probe_socket.connect((target,port))
                request = f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode('utf-8')
                probe_socket.send(request)
        
                banner = probe_socket.recv(10240)
                if len(banner) > 0:
                    print(f"Received HTTP 200: {banner[0:9].decode("utf-8")}, on Port: {port}")
            except:
                pass

            try:
                probe_socket.connect_ex((target,port)) #Just Connecting to gather the information
                service = socket.getservbyport(port)
                print(f"\nRunning Service: {service} on Port: {port}\n")
            except:
                pass
        else:
            pass
    except Exception as e:
        pass
    finally:
        probe_socket.close()


def Scanport(target,port):
    try:
        sock_sniff= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_sniff.setblocking(False)
        sock_sniff.settimeout(10)
        result = sock_sniff.connect_ex((target,port)) #Error handler, if 0 = port open
        if result == 0:
            #time.sleep(2) #Slow down the Scan. Disable for Aggressive Scanning.
            print(f"Port [{port}]-is open")
            ProbeVersion(target=target,port=port)
        else:
            pass

        time.sleep(1)   
        sock_sniff.close()

    except socket.error:
        print(f"Socket Error on port {port}: {socket.error}")
        
    except Exception as e:
        print(f"ERROR , ErrorCode: {e}")

#Main Function - argument validation
def main():
    slowdown = threading.Event()
    #Prety Banner
    print("""

███████╗██╗  ██╗██╗   ██╗███████╗████████╗██╗  ██╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ 
██╔════╝██║  ██║██║   ██║██╔════╝╚══██╔══╝██║  ██║██╔════╝██║    ██║██╔═████╗██╔══██╗██║     ██╔══██╗
███████╗███████║██║   ██║█████╗     ██║   ███████║█████╗  ██║ █╗ ██║██║██╔██║██████╔╝██║     ██║  ██║
╚════██║╚════██║╚██╗ ██╔╝██╔══╝     ██║   ██╔══██║██╔══╝  ██║███╗██║████╔╝██║██╔══██╗██║     ██║  ██║
███████║     ██║ ╚████╔╝ ███████╗   ██║   ██║  ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝
╚══════╝     ╚═╝  ╚═══╝  ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ 
                                                                                                     
          """)
    

    if len(sys.argv) == 1: #Checking for 2 arguments in the cli, including name of the Script
        #target = sys.argv[1]
        pass
    else:
        print("Invalid Number of Arguments\nEnter Target-Adress.")
        sys.exit(1)
    
    try:
        target_ip = input("Input IP to Scan: ")
    except socket.gaierror:
        print(f"Inavlid Hostname, cannot resolve Hostname-Target: {""}")
        sys.exit(1)
    except KeyboardInterrupt:
        print(f"\n-EXITING-\nFOLLOW THE RABBIT\nH\n\nO\n\n\nL\n\n\n\nE")
        sys.exit(1) #We stop the programm, we dont want it to continue 
    
    print(f"Scanning Target: {target_ip}\nTime Started: {datetime.now()}")
    try:
        for port in range (1,65536):
            threads = []
            thread = threading.Thread(target=Scanport, args=(target_ip, port)) #target executes the function with the thread, the arguments are going to be the args poassed down in the thread
            threads.append(thread)
            thread.start()
            
           
            
        
        for thread in threads: #Thread List contains all the thread objects.
            thread.join() #Syncing, best practice, make sure all the things work.
            ProbeVersion(target=target_ip,port=port)

        
        print("\n\nScan Completed.\nWritten by Zin0d\nSpecial_Thanks to TCM-ACADEMY.")

    except:
        pass


if __name__ == "__main__":
    main()