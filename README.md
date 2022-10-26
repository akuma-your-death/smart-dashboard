# smart-dashboard Version: 0.1.3
#
##How to run:
##
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
+ git clone https://github.com/akuma-your-death/smart-dashboard
+ cd smart-dashboard
+ pip install -r requirements.txt
+ python3 dashboard.py 
+ write your gateway
+ open new terminal and write python3 nmap.py
+ open new terminal and write python3 server.py
+ if you are not automatically forwarded to your browser then just type on your browser http://(your IPv4):8000
###

### Updates:

imaginations for 1.0.0 - 2.0.0 update:
+ more things possible to do
+ replacement for txt files to one big json file
+ works automaticly for linux
+ i'll try to make it also for termux automaticly

0.1.3 updates (2022-26-10):
+ update for checking if gateway isnt right(still not 100%)
+ fixed nmap bugs(i didnt noticed these bugs thats why i patched them so lately)
+ working nice on linux but you have to run manuelly dashoabord.py then nmap.py and then server.py on different terminals

0.1.2 updates (2022-24-10):
+ tells you if gateway isnt right
+ works for linux but not automaticly

0.1.1 updates (2022-23-10):
+ auto ping-test (html file)
+ now you can set new nmap target without waiting till the website loads (target will be scaned after homenetwork)
- still doesnt working for linux

0.1.0 updates (2022-23-10):
+ better look (html file)
+ bug fix with nmap
- still doesnt working with linux

this is my first python tool i would love feedback and new ideas.
Run only dashboard.py the rest will be created and run by themself
On Linux you have to run run-if-linux.sh or run manuelly dashboard.py, nmap.py and server.py (i'll add this bash file in maybe 0.1.3 update (notice on 2022-25/30-10))

if you install the requirements.txt its not a problem if you get only errors, these tools should be install by standard but just to be safe

made with ❤️ from akuma-your-death
