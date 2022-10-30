from datetime import datetime
import os
import socket
import webbrowser
import http.server
import socketserver
import time
import webbrowser
import platform
import os
now = datetime.now()
pyautoguipip = True
try:
    import pyautogui
except ModuleNotFoundError as error:
    import keyboard
    pyautoguipip = False
os.system('cls||clear')

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

try:
    with open("PyWhatKit_DB.txt", "r") as file:
        PyWhatKitDB = file.read()
    if PyWhatKitDB == "":
        with open("PyWhatKit_DB.txt", "w") as file:
            file.write("no sendet msg")
except FileNotFoundError as error:
    with open("PyWhatKit_DB.txt", "w") as file:
        file.write("no sendet messages write send wa msg in dashboard.py")

with open("start_website.txt", "w") as file:
    file.write("3")
    
with open("target2.txt", "w") as file:
    file.write("3")

with open("nmap_target_answer.txt", "w") as file:
    file.write("set first a target in dashboard.py")

with open("target.txt", "w") as file:
    file.write("0")

sys = platform.system()
if sys[:3] == "Win":
    os.system("start /min cmd /k python server.py")
# Webserver Port
port = 8000

# IPv4 for webserver 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]

with open("ip-client.txt", "w") as file:
    file.write(ip)

ip_for_proof = ip[:4]
last_number_ip_for_proof = ".1"

routers_website = input(str("whats your standart gateway?(its your ip but the last number*s is a 1 if you dont know your IP write ip)(XXX.XXX.XXX.1) "))

with open("start_website.txt", "w") as file:
    file.write("1")

time.sleep(5)

with open("start_website.txt", "w") as file:
    file.write("3")

charackter_number = len(routers_website)

if charackter_number <= 7 and routers_website != "ip":
    not_okay_ip = False
else:
    not_okay_ip = True
    
if charackter_number >= 15 and routers_website != "ip":
    not_okay_ip = False
else:
    not_okay_ip = True
    
if routers_website == "ip":
    print(ip)

if routers_website[:4] == ip_for_proof and routers_website[-2:] == last_number_ip_for_proof and not_okay_ip == True:
    everthing_okay = True
    if charackter_number <= 7 and routers_website != "ip":
        not_okay_ip = False
    else:
        not_okay_ip = True
    
    if charackter_number >= 15 and routers_website != "ip":
        not_okay_ip = False
    else:
        not_okay_ip = True

    with open("routers_ip.txt", "w") as file:
        file.write(routers_website)
else:
    everthing_okay = False

while everthing_okay == False or routers_website[:4] != ip_for_proof and routers_website != last_number_ip_for_proof[-2:] or routers_website != "ip" or routers_website == "ip" and routers_website != charackter_number:
    charackter_number = len(routers_website)
    if routers_website[:4] == ip_for_proof and routers_website[-2:] == last_number_ip_for_proof:
        with open("routers_ip.txt", "w") as file:
            file.write(routers_website)
        break
    else:
        routers_website = input("write ip or your standard gateway ")
    with open("proof.txt", "w") as file:
        file.write(routers_website)
    with open("proof.txt", "r") as file:
        routers_website = file.read()
    if routers_website == "ip":
        print(ip)

if routers_website == "":
    with open("routers_ip.txt", "r") as file:
        routers_website = file.read()
# Sets Routers IP the same as in the input 
with open('routers_ip.txt','r') as file:
    routers_website = file.read()
if sys[:3] == "Win":
    os.system("start /min cmd /k python nmap.py")
if sys[:3] == "Lin":
    os.system('xterm -3 python3 nmap.py')
print("pleas wait for like 1 minute while creating file and starting nmap(you can watch one of my german Videos on youtube while that https://www.youtube.com/watch?v=ANXkX6ixaxg)")


# Creates index.html if it doesnt exist and writes html code in it 
with open("index.html", "w") as file:
    file.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css">
    <meta http-equiv="refresh" content="30" />
    <meta charset="UTF-8"> 
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h3 style="color: white; text-align: center;">The time is: <span id="time" style="color: white;"> </span></h3>
        <h4 style="color: white; text-align: center;">your wifi is <span id="wifi_speed"> </span>MB's fast (but on a local file thats why its more then normal)</h4>
        <button class="glow-on-hover" type="button" onclick="window.location.href ='http://192.168.178.1'">
            <span style="color: white;">
                log to your Router in
            </span>
        </button>
    <p>
        <button class="glow-on-hover" type="button" onclick="window.location.href ='network_ips.txt'">
            <span style="color: white;">
                <p>
                    show all ips from network
                </p>
            </span>
        </button>
        <p>
            <button class="glow-on-hover" type="button" onclick="window.location.href='nmap_target_answer.txt'">                
                <span style="color: white;">
                    <p>
                        get Target's nmap report (write nmap in dashoard.py)
                    </p>
                </span>            
            </button>
        </p>
            <button class="glow-on-hover" type="button" onclick="window.location.href='PyWhatKit_DB.txt'">
                <span style="color: white;">
                    <p>
                        get last sendet messages(wa)
                    </p>
                </span>
            </button>
        
</body>
<script src="java.js">

</script>
</html>
""")

while True:
    try:
        with open("network_ips.txt", "r") as file:
            network_ips = file.read()
    except FileNotFoundError as file_not_found:
        pass
    mode = input("choose mode ")
    if mode == "nmap":
        nmap_target = input("target ip ")
        with open("target.txt", "r") as file:
            target_True = file.read()
        if target_True == "0" and nmap_target != "":
            with open("target2.txt", "w") as file:
                file.write("1")
        with open("target.txt", "w") as file:
            file.write("1")
        with open("nmap_target_ip.txt", "w") as file:
            file.write(f"{nmap_target}")
    
    if mode == "send wa msg":
        number = input("contact number: ")
        message = input("message: ")
        webbrowser.open(f"web.whatsapp.com/send?phone={number}&text={message}")
        # if your wifi is bad or faster just change the number (time.sleep(1) = timeout for 1 second)
        time.sleep(7)
        if pyautoguipip != False:
            pyautogui.press("enter")
            pyautogui.keyDown("alt")
            pyautogui.press("f4")
            pyautogui.keyUp("alt")
        else:
            keyboard.press_and_release('enter')
            keyboard.press_and_release('alt + f4')
            
        with open("PyWhatKit_DB.txt", "w") as file:
            file.write(f"message: {message} to {number} at {day}.{month}.{year} at {hour}:{minute}.{second}")