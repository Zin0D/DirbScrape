#! /usr/bin/env python3
import queue
import requests
import os
import threading
import time
from tqdm import tqdm

AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" #Trick the Server.
EXTENSIONS = [".php",".bak",".txt",".inc",".orig",".js",]
TARGET = "http://testphp.vulnweb.com" #Without /, or you get goofy output bro. 
THREADS = 20  
WORDLIST = "apache.txt" #Input your Wordlist Path
parsed_list = [] #All Objects, 200
PROXIE = { #Configuring the Tor Proxy.
    "http" : "socks5h://127.0.0.1:9050",
    "https" : "socks5h://127.0.0.1:9050"
}

""" Use Proxies to route through TRAFFIC! """
testing_IfTorTrue = 'https://check.torproject.org/' #Save for later use cases.


def get_words():
    words = queue.Queue() #List for each word to be appended to
    def extend_words(word):
        if "." in word: #If its a file, (since we appended stuff into the queque with .)
            words.put(f'/{word}') 
        else:
            words.put(f'/{word}/') #If dir, then put it into a queque with a /

        for extensions in EXTENSIONS:
            words.put(f'/{word}{extensions}') #Trying to test out extensions for each word aswell.
    
    with open(WORDLIST) as f:
        content_all = f.read()
   
    for word in tqdm(content_all.split()): #Put all the Words of that file, into a List .split() to iterrate over it.
        #print(word)
        extend_words(word) #Parse the Word of the List into the function, that sends a request on a newly generated Thread.
    return words #Returns the Quequqe

#How Queque Should look like, for each Element x inside of the Wordlist.
#FIFO principle
""" [
    '/hello/',    # as a directory
    '/hello.php', # file with .php extension
    '/hello.bak', # file with .bak extension
    
    '/hello.txt', # file with .txt extension
    '/hello.inc', # file with .inc extension
    '/hello.orig',# file with .orig extension
    '/hello.js'   # file with .js extension
]"""

def readd(recurse, words):
    if "." not in recurse:
        formatted_recurse = recurse.replace("/","",2)
        #print(formatted_recurse)
        with open(WORDLIST) as e:
            content = e.read()
        for x in content.split():
            words.put(f"/{formatted_recurse}/{x}") #
            for i in EXTENSIONS:
                words.put(f"/{formatted_recurse}/{x}{i}")
    # NEED TO PARSE THE RECURSE to the function extend_words.
    # Only need 200 to Append, so will leave out all the other.

    
def brutforcer(words):
    
    headers = {'User-Agent' : AGENT}
    while not words.empty(): #As Long as the queque is not over.
        recurse = words.get()
        Link = f'{TARGET}{recurse}' #Fetches the String 
        try:
            contents_http = requests.get(Link,headers,timeout=10) #Mimic a Legit user :D
            time.sleep(0.2) 
        except requests.exceptions.ConnectionError as Error: 
            print(f"Something went Wrong: {Error}")
        
        match contents_http.status_code:
            case 200:
                print(f"New Discovery [X] ({contents_http.status_code} : {Link})")
                #print(recurse)
                parsed_list.append(Link)

                readd(recurse=recurse,words=words) #Just use a function nixher

            case 301:
                pass

            case 302:
                pass
            
            case 307:
                pass

            case 404:
                pass                

    return parsed_list

def host_list():
    e = open('links.txt', 'a') 
    for each_element in parsed_list:
        e.write(f"{each_element}\n")

def clean_files():
    try:
        os.remove('links.txt')
    except:
        pass
    
def start_threads():
    thread_count = THREADS
    words = get_words()
    threadss = []

    for _ in range(thread_count):
        #time.sleep(0.5) //ASK Ecurve.
        thread = threading.Thread(target=brutforcer,args=(words,))
        thread.start()
        threadss.append(thread)
    
    for x in threadss:
        x.join()
        

if __name__ == "__main__":
    start_threads()
    host_list()
    
