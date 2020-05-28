#!/usr/bin/env python3
import os, sys, mimetypes
from socket import *
if int(sys.version[0]) != 3:
    print("E: Python 3.x is required")
    sys.exit(1)
print("sesHTTPD")
print("By Nitin Seshadri\n")
try:
    port = int(sys.argv[1])
except:
    port = 0
serversocket = socket(AF_INET, SOCK_STREAM)
try:
    serversocket.bind(("", port))
except:
    print("W: Could not bind to port", port, "-- choosing a random one instead\n")
    port = 0
    serversocket.bind(("", port))
serversocket.listen(5)
ip = serversocket.getsockname()[0]
port = serversocket.getsockname()[1]
print("Launched web server on", ip, "port", port)
url = "http://localhost:" + str(port)
print("Local URL:", url)
print("Press CTRL-C to quit.\n")
while True:
    try:
        (clientsocket, address) = serversocket.accept()
        data = clientsocket.recv(1024).decode("utf-8")
        if not str(data):
            data = "GET / HTTP/1.1" #HACK: Handle empty requests
        localfile = data.split("\n")[0].split(" ")[1].split("/",1)[1].split("?")[0].replace("%20", " ")
        if localfile == "":
            localfile = "index.html"
        if os.path.isdir(localfile):
            localfile = localfile.rstrip("/") + "/index.html"
        if os.path.isfile(localfile):
            print("GET", localfile, "200 OK -", str(address[0]))
            clientsocket.send(b"HTTP/1.1 200 OK\r\n")
            contenttype = mimetypes.guess_type(localfile, strict=True)
            contenttype = contenttype[0]
            contenthdr = "Content-Type:" + str(contenttype) + "\r\n\r\n"
            contenthdr = contenthdr.encode("utf-8")
            clientsocket.send(contenthdr)
            filedata = open(localfile, "rb")
            output = filedata.read()
            clientsocket.send(output)
            filedata.close()
            clientsocket.shutdown(1)
        else:
            print("GET", localfile, "404 Not Found -", str(address[0]))
            clientsocket.send(b"HTTP/1.1 404 Not Found\r\n")
            clientsocket.send(b"Content-Type: text/html\r\n\r\n")
            clientsocket.send(
                b"<HTML><HEAD><TITLE>404 Not Found</TITLE></HEAD><BODY><H1>404 Not Found</H1></BODY></HTML>")
            clientsocket.shutdown(1)
    except ConnectionAbortedError:
        pass
    except KeyboardInterrupt:
        print("\nW: Interrupt received, stopping...")
        serversocket.close()
        sys.exit(0)
