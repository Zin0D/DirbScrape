# BrutForce Directory Script

This script is designed for brute-forcing directories during penetration testing. It includes the capability to route requests through the Tor network, providing an added layer of anonymity. However, configuring Tor support requires manual adjustment.

## Disclaimer

**This script is intended for ethical hacking and authorized penetration testing only.** Unauthorized use is illegal and unethical. If you engage in illegal activities with this tool, the responsibility is solely yours.


## Features

- Directory brute-forcing, content scraping of found links.
- Supports manual configuration for routing through Tor by modifying the proxy settings in the `requests.get()` function. 
- Due to routing traffic through a Socks5h proxy (Force DNS Resolve on the side of the proxy), its best adviced to also turn off dns locally, (Depending on what you do :P)

## WHY PUBLISH?

- Same reason why everybody else publishes their stuff, missuse of the tool is not a problem of the creator.