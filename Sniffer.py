import socket
from scapy.all import IP, ICMP, TCP, sr1, sniff
import argparse
import ipaddress
import struct
import sys

""" Wir spannen den Server, und starten ihn via die listen function,
    Daraufhin müssen wir in einem Loop dauerhaft auf eine Verbindung warten"""

print(f"PWN THE SYSTEM\nFOLLOW THE RABBIT\nH\n\nO\n\n\nL\n\n\n\nE")


parser = argparse.ArgumentParser(description=
"Network Packet Sniffer :D\n Built in Python")
parser.add_argument('-i',type=str, help="Provide the Adress to Sniff on", required=True)
opts = parser.parse_args()

class Packets:
    def __init__(self, data): #Parsing the packet and extracting it,
        self.int_packet = data
        header = struct.unpack('!BBHHHBBH4s4s', self.int_packet[:20]) #Total 20 Bytes is the Ip header
        self.ver = header[0] >> 4 
        self.ihl = header[0] & 0xF 
        self.tos = header[1]
        self.ls = header[2]
        self.id = header[3]
        self.flags = header[4] >> 13 
        self.fo = header[4] & 0x1FFF 
        self.ttl = header[5]
        self.pro = header[6] #Checking for the Version Protocol
        self.num = header[7]
        self.src = header[8]
        self.dst = header[9]

        self.src_addr = ipaddress.ip_address(self.src)
        self.dst_addr = ipaddress.ip_address(self.dst)

        self.protocol_map = {1 : "ICMP",6: "TCP",17: "UDP"} #Value 1 is for ICMP Defined by Iana

        try:
            self.protocol = self.protocol_map[self.pro] #Checking if ICMP is included
        except Exception as e:
            print(f'{e} No Protocol {self.protocol_map[1]} ')
            self.protocol_map = str(self.pro)
            print(self.protocol_map)
    
    def output(self):
        print(f"Protocol Used:[{self.protocol}], FROM IP:[{self.src}] - - TO - - IP:[{self.dst}]")


#Sniffing Function is simple.
def sniff(host):
    socket_icmp = socket.IPPROTO_ICMP #ICMP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_icmp)
    sniffer.bind((host, 0)) #0 We not listening on a socket.
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    try:
        while True:
            raw_data = sniffer.recv(65535)
            packet = Packets(raw_data) #Parsing Raw_data to Class
            packet.output()

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        sys.exit(1)

#Constructing a Syn packet via scapy

''' ADDITIONAL STUFF ON THE BOTTOM '''
def syn_check():
    packet = IP(dst="") / TCP(dport=80, flags="S") #Shit it worked

    response = sr1(packet)
    response.show()
    print("[READY TO START]\n-",len("Ready to start")*"-","-")

def server_starting(ip = "127.0.0.1", port = 5021):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port ))
    server.listen(3)

    while True:
        c_sock , c_addr = server.accept()

        print(f"Connected: {c_addr}")

        message = c_sock.recv(2048)
        print(message.decode('utf-8'))

        c_sock.send("Received Connection".encode('utf-8'))


# Sniffing von Packeten via Mac-Adresse :D A Key Logger huh?
if __name__ == '__main__':
    sniff(opts.i) #We parsed the Argument Handler to opts, which now we can specify the input of our cli.

