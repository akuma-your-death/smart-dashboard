import os
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ipV4 = s.getsockname()[0]
ip_for_proof = ipV4[:12]


while True:
    with open("target2.txt", "r") as file:
        target2 = file.read()
    with open("target.txt", "r") as file:
        nmap_target = file.read()
        if nmap_target == "0":
            with open("start_website.txt", "w") as file:
                file.write("0")
            with open("routers_ip.txt", "r") as file:
                ip = file.read()
            if ip[12:] != ip_for_proof:
                pass 
            network_ips = os.system(f'nmap -oN network_ips.txt {ip}/24')

            with open("start_website.txt", "w") as file:
                file.write("1")

            with open("target.txt", "w") as file:
                file.write("3")
            time.sleep(1)
            with open("start_website.txt", "w") as file:
                file.write("3")
    if nmap_target == "1" or target2 == "1":
        time.sleep(1)
        with open("nmap_target_ip.txt", "r") as file:
            target = file.read()
        nmap_target_answer = os.system(f'nmap -oN nmap_target_answer.txt {target}')
        with open("nmap_finish.txt", "w") as file:
            file.write("1")
        with open("target.txt", "w") as file:
                file.write("3")
        with open("target2.txt", "w") as file:
            file.write("3")
        time.sleep(1)
        with open("nmap_finish.txt", "w") as file:
            file.write("3")
    if nmap_target == "3":
        pass