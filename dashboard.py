import os
import socket
import webbrowser
import http.server
import socketserver
import time
import webbrowser
import platform

with open("target.txt", "w") as file:
    file.write("0")

sys = platform.system()
if sys[:3] == "Win":
    os.system("start /min cmd /k python server.py")
if sys[:3] == "Lin":
    os.system('xterm -3 python3 server.py')
# Webserver Port
port = 8000

# IPv4 for webserver 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]

with open("ip-client.txt", "w") as file:
    file.write(ip)

routers_website = input(str("whats your standart gateway?(its your ip but the last number*s is a 1 if you dont know your IP write ip but for only one time)(XXX.XXX.XXX.1) "))
if routers_website == "":
    with open("routers_ip.txt", "r") as file:
        routers_website = file.read()    
# Writes input from Router IP to routers_ip.txt
with open("routers_ip.txt", "w") as file:
    file.write(f"{routers_website}")
# Sets Routers IP the same as in the input 
with open('routers_ip.txt','r') as file:
    routers_website = file.read()
with open("network_ips.txt", "r") as file:
    network_ips = file.read()
if routers_website == "ip":
        print(ip)
        routers_website = input(str("whats your standart gateway?(XXX.XXX.XXX.1) "))
        with open("routers_ip.txt", "w") as file:
            file.write(f"{routers_website}")
        # Sets Routers IP the same as in the input 
        with open('routers_ip.txt','r') as file:
            routers_website = file.read()
        with open("network_ips.txt", "r") as file:
            network_ips = file.read()
if sys[:3] == "Win":
    os.system("""
start /min cmd /k python nmap.py
""")
if sys[:3] == "Lin":
    os.system('xterm -3 python3 nmap.py')
print("pleas wait for like 1 minute while creating file and starting nmap(you can watch one of my german Videos on youtube while that https://www.youtube.com/watch?v=ANXkX6ixaxg)")


# Creates index.html if it doesnt exist and writes html code in it 
with open("index.html", "w") as file:
    file.write(f"""
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="refresh" content="30" />
    <meta charset="UTF-8"> 
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h3>The time is: <span id="time"> </span></h3>
    <button style="border-radius: 10px; background-color: black;" >
        <a href="http://{routers_website}">
            <span style="color: white;">
                <p>
                    log to your Router in
                </p>
            </span>
        </a>
    </button>
    <p>
        <button style="border-radius: 10px; background-color: black;" >
            <a href="network_ips.txt">
                <span style="color: white;">
                    <p>
                        show all ips from network
                    </p>
                </span>
            </a>
        </button>
        <p>
            <button style="border-radius: 10px; background-color: black;">
                <a href="nmap_target_answer.txt">
                    <span style="color: white;">
                        <p>
                            get Target's nmap report (write nmap in dashoard.py)
                        </p>
                    </span>
                </a>
            </button>
        </p>
</body>
<script src="java.js">

</script>
</html>
""")

while True:
    mode = input("choose mode (pleas wait until the website loads) ")
    if mode == "nmap":
        nmap_target = input("target ip ")
        with open("target.txt", "w") as file:
            file.write("1")
        with open("nmap_target_ip.txt", "w") as file:
            file.write(f"{nmap_target}")
        with open("nmap_finish.txt", "r") as file:
            nmap_finish = file.read()
        if nmap_finish == "1":
            with open("target.txt", "w") as file:
                file.write("3")
            with open("nmap_target_answer.txt", "r") as file:
                nmap_answer = file.read()
            if nmap_answer == "":
                pass
            if nmap_answer != "":
                os.system('start /min cmd /k python update_website.py')