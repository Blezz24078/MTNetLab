# PLEASE READ THIS FIRST:
# DISCLAIMER: THIS PROGRAM IS FOR AUTHORIZED, LEGAL USE ONLY. BY DOWNLOADING THIS FILE, YOU ARE LIABLE FOR ANY DAMAGE CAUSED TO YOURSELF OR OTHERS.

# MTNetLab
This set of programs is used for some basic pentesting along with arduino HID code, and more.

# GITRECONVIRUS.py [2.0.1]
This virus is VERY HARMFUL if misused.
If you run it right after downloading, nothing will happen. This is because it's unarmed. This is to keep the virus from getting accidentally run. There *are* some comments that should stay, it's fine to remove them.
THIS IS NOT FULY TESTED, NO GAURANTEED RESULTS.

HOW TO ARM:
- Un-hashtag all of the code
- Remove the print(removetoarm)
- It's armed

What this program does:
- Sets the mouse to the coordinates (100, 100) on the screen 10 times/second
- Deletes all files on device
- Uses multiprocessing to complete both at once
- Checks OS for proper commands
- Checks if modules are installed, and tries to install necesary modules if they are not installed

# IP_SCRAPER.py [2.0.0]

This python program is used for scraping IP addresses in a selected range. It will ask for the First and second octets. Ex: (10.1). After, it will let you choose the range for the 3rd octet (xx.x.12.xxx). Ex: 12 - 15. Then, after the scan is complete, it will print out the status of each IP in the selected range. Ex: 10.1.28.188 is live, Hostname: Unknown, RTT: 24.56ms It shows if it's live, attempts to find the hostname, and shows the ping response time.

# MALWAREFORARD.ino [ALPHA]

This is an Arduino program. I programmed it specifically for the Arduino Leonardo on MacOS. I chose the Leonardo because it's fairly optimal for being an HID.
Testing and updates for the BadUSB will be released but right now it should work well on the Leonardo.

Right now, it isn't very destructive. It's really just a framework for destruction. As of right now, it just will rick roll whoever plugs it into their MacBook. For more power, remove the link to that git download and switch it to a different program.

# BadUSBProgrammer.py [ALPHA TESTING]

This is a python program that's used for writing keypress code for HID Arduino boards. As in the name, it's being made for the BadUSB. This code is NOT complete, but I thought that it would be useful to include. There are some syntax errors in the output (That's the issue).

# Password Generator V.2.py [BETA]

This python program is for generating secure, 8 character+ passwords.

# wiresharkfilefinder.py [ALPHA]

This python program is used for finding specific hostnames in a .pcapng wireshark file. It's for the mdns set of hostnames.

How to use:
1) Input path to file
2) Input hostname for search

This will return all of the instances of the hostname. Each one is the hostname's IP and the target IP. After each search, you can enter the number of the instance and it will give a more detailed report about it.

# linuxonmac.sh [0.1]
*THIS PROGRAM IS ON ITERATION 1. PLEASE DO NOT RELY ON THIS WORKING AS IT MIGHT NOT.*

This program is intended to make it easier to get a pretty complete kali toolkit on mac.

HOW TO USE:
1) I would reccomend to just copy the script from the repo instead of downloading it
2) run this in terminal: "nano program.sh" (Without the quotation marks).  It will create a new file.
3) Paste the script into the text editor thing that shows up
4) when you're done, ctrl+x, y, enter
5) run "chmod +x program.sh"
6) finally, run "./program.sh"
7) Wait for it to finish



# Tools

BadUSB: [Link(Amazon)](https://www.amazon.com/HiLetgo-Microcontroller-ATMEGA32U4-Development-Keyboard/dp/B07W5K9YHP/ref=sr_1_3?crid=29M2WRQG8TGGF&dib=eyJ2IjoiMSJ9.Hpwk6iwFbiSswVO61_3VvO0ucUmlpjBpiNVimVsJDET_YGL2XmddelZeAqlkY2VEUPkFhMQ9MaqAiH4Zvr4rSBT7hCgTM1_GkQtMiGEweTqD31zHufs3uRC5khZSfFgk5wB7T9bZOfdDZxwFIu98FIb3sfzOxnTgPQRZLB7s_de96zLpOZi1BuHRlOShsq8V-eq5UdPq2Xr7r4uyE3F0wbwsi7SzEGz1BoL2GHHTKF8.wjk8jUDgslJAg6cGqMliEjliQ1G6mbHii3-2xVZo1vc&dib_tag=se&keywords=badusb&qid=1764869076&sprefix=badusb%2Caps%2C119&sr=8-3)

# RECOMMENDED SOFTWARE

ARDUINO IDE:

This is used for compiling and uploading code onto arduinos. This is needed to use the BadUSBProgrammer.py and the MALWAREFORARD.ino
[Link](https://www.arduino.cc/en/software/)

Python IDLE or Visual Studio Code (VSCode):

This is used for running all of the .py files. In order to use virtually all of the programs here.

[IDLE](https://www.python.org/downloads/)

[VSCode](https://code.visualstudio.com/)

Wireshark:

Wireshark is used to capture wifi traffic on the network you are connected to. It will track hostname, target, and other information.

PLEASE NOTE: IT IS **ILLEGAL** TO USE WIRESHARK OR ANY OTHER IP SCRAPER TYPE OF PROGRAM WITOUT EXPLICIT CONSENT FROM THE NETWORK OWNER

[Wireshark](https://www.wireshark.org/)

[Tor:]

Tor is a browser based on anonymity. It's fairly slow, but is virtually untraceable. It is recommended to use a VPN while using Tor. Tor is used by anybody who wants to communicate anonymously, or people who want to open .onion links. Tor's nickname is "The Onion" because of this. Please note that illegal activity does occur on Tor and links could download malware. Make sure that you trust the website before downloading ANYTHING for safety.

To download, go to Torproject.org
