import webbrowser
import socketserver
import http.server
import time

port = 8000
while True:
    with open("ip-client.txt", "r") as file:
        ip = file.read()
    time.sleep(1)
    with open("start_website.txt", "r") as file:
        start_browser = file.read()
    if start_browser == "1":
        Handler = http.server.SimpleHTTPRequestHandler
        print(f"click here to get to graphical dashboard: http://{ip}:8000")
        webbrowser.open(f"http://{ip}:8000")
        with socketserver.TCPServer(("", port), Handler) as httpd:
            httpd.serve_forever()
    if start_browser == "3":
        pass