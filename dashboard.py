import os
import socket
import webbrowser
import http.server
import socketserver
import time
import webbrowser
import platform

sys = platform.system()

# Webserver Port
port = 8000

# IPv4 for webserver 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]

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
    <link rel="stylesheet" href="style.css">
    <meta http-equiv="refresh" content="30" />
    <meta charset="UTF-8"> 
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h3>The time is: <span id="time"> </span></h3>
    <button class="router_ip">
        <a href="http://{routers_website}">
            log to your Router in
        </a>
    </button>
    <p>
    <button class="network_ips">
        <a href="network_ips.txt">
    show all ips from network (needs wifi to do and some time)
        </a>
    </button>
</body>
<script src="java.js">

</script>
</html>
    """)

while True:
    time.sleep(1)
    with open("start_website.txt", "r") as file:
        start_browser = file.read()
    if start_browser == "1":
        Handler = http.server.SimpleHTTPRequestHandler
        print(f"click here to get to graphical dashboard: http://{ip}:8000")
        webbrowser.open(f"http://{ip}:8000")
        with socketserver.TCPServer(("", port), Handler) as httpd:
            httpd.serve_forever()