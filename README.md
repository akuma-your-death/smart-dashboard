# smart-dashboard Version: 0.1.3

## How to run:

### Windows:
+ download nmap(https://nmap.org/dist/nmap-7.93-setup.exe")
+ setup nmap
+ download zip folder(this script not from nmap)
+ go to downloads and unzip it
+ open terminal and write cd (path/to/smart-dashboard)
+ pip install -r requirements.txt
+ python dashboard.py
###
### Linux
+ sudo apt install nmap
+ git clone https://github.com/akuma-your-death/smart-dashboard
+ cd smart-dashboard
+ pip install -r requirements.txt
+ python3 dashboard.py 
+ write your gateway
+ open new terminal and write python3 nmap.py
+ open new terminal and write python3 server.py
+ if you are not automatically forwarded to your browser then just type on your browser http://(your IPv4):8000
###

## Updates:

### imaginations until 1.0.0 - 2.0.0 update:
+ more things possible to do
+ replacement for txt files to one big json file
+ works automaticly for linux

### 0.1.3 updates (2022-30-10):
+ write send wa msg in dashboard.py select number and message and press enter (the script will automaticly press enter and ALT + F4 to close window after 7 seconds if you need more/less time bc of your wifi then change the number at row 213)
+ you can see the last sendet message at the html file (with number, message and date)

### 0.1.2 updates (2022-26-10):
+ update for checking if gateway isnt right(still not 100%)
+ fixed nmap bugs(i didnt noticed these bugs thats why i patched them so lately)
+ working nice on linux but you have to run manuelly dashoabord.py then nmap.py and then server.py on different terminals

### 0.1.1 updates (2022-24-10):
+ tells you if gateway isnt right
+ works for linux but not automaticly

### 0.1.0 updates (2022-23-10):
+ auto ping-test (html file)
+ now you can set new nmap target without waiting till the website loads (target will be scaned after homenetwork)
+ better look (html file)
+ bug fix with nmap
- still doesnt working with linux

this is my first python tool i would love feedback and new ideas.
Run only dashboard.py the rest will be created and run by themself
On Linux you have to run run-if-linux.sh or run manuelly dashboard.py, nmap.py and server.py

if you install the requirements.txt its not a problem if you get only errors, these tools should be install by standard but just to be safe

if you want to send whatsapp messages at first you have to login in web.whatsapp.com with your stanrd browser(mine is chrome) 

made with ?????? from akuma-your-death
