import network
import socket
from machine import Pin
import time
import os

SSID = "GunnarPC"
PASSWORD = "Hemmelig"

led = Pin(2, Pin.OUT)

# CONNECT WIFI
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Disable power saving → improves responsiveness
try:
    wifi.config(pm=0xa11140)
except:
    pass

wifi.connect(SSID, PASSWORD)

print("Connecting...")
while not wifi.isconnected():
    time.sleep(0.1)

print("Connected!", wifi.ifconfig())

# MIME TYPES
def content_type(filename):
    if filename.endswith(".html"):
        return "text/html"
    if filename.endswith(".css"):
        return "text/css"
    if filename.endswith(".js"):
        return "application/javascript"
    return "text/plain"

# SEND FILE IN CHUNKS (IMPORTANT)
def send_file(client, filepath):
    try:
        size = os.stat(filepath)[6]

        header = """HTTP/1.1 200 OK\r
Content-Type: {}\r
Content-Length: {}\r
Connection: close\r
\r
""".format(content_type(filepath), size)

        client.send(header)

        with open(filepath, "rb") as f:
            while True:
                chunk = f.read(512)
                if not chunk:
                    break
                client.send(chunk)

    except Exception as e:
        client.send(b"HTTP/1.1 500 Internal Server Error\r\n\r\n")
        print("File send error:", e)

# READ HTTP REQUEST SAFELY
def read_request(client):
    client.settimeout(1.5)

    data = b""
    try:
        while True:
            chunk = client.recv(512)
            if not chunk:
                break
            data += chunk

            # End of headers
            if b"\r\n\r\n" in data:
                break
    except:
        pass

    return data.decode("utf-8", "ignore")

# SERVER SETUP
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(addr)
server.listen(2)

# Accept timeout → prevents blocking forever
server.settimeout(1)

print("Server running")

while True:
    try:
        client, addr = server.accept()
    except:
        continue

    print("Client connected:", addr)

    request = read_request(client)

    if not request:
        client.close()
        continue

    try:
        path = request.split(" ")[1]
    except:
        client.close()
        continue

    # GPIO TOGGLE
    if path == "/toggle":
        led.value(not led.value())
        response = b"ON" if led.value() else b"OFF"

        client.send(b"""HTTP/1.1 200 OK\r
Content-Type: text/plain\r
Connection: close\r
\r
""" + response)

    else:
        if path == "/":
            path = "/index.html"

        filepath = "/www" + path

        if filepath.endswith("/"):
            filepath += "index.html"

        try:
            send_file(client, filepath)
        except:
            client.send(b"""HTTP/1.1 404 NOT FOUND\r
Content-Type: text/plain\r
Connection: close\r
\r
404 File Not Found""")

    client.close()