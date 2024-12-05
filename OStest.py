#!/usr/bin/env python3

import requests
PROXIE = { #Configuring the Tor Proxy.
    "http" : "socks5://127.0.0.1:9050",
    "https" : "socks5://127.0.0.1:9050"
}
x = requests.get("https://google.com",proxies=PROXIE,timeout=10)
