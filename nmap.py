import os
import time

with open("start_website.txt", "w") as file:
    file.write("0")

with open("routers_ip.txt", "r") as file:
    ip = file.read()
network_ips = os.system(f'nmap -oN network_ips.txt {ip}/24')

with open("start_website.txt", "w") as file:
    file.write("1")

time.sleep(1)
with open("start_website.txt", "w") as file:
    file.write("0")
os.system('exit')