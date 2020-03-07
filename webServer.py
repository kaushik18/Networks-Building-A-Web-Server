# Kaushik Nadimpalli
# Cs4390.502
# Assignment 1 - Question 5

# Imports 
import socket
from socket import *

serverSocket = socket(AF_INET,SOCK_STREAM) # TCP Welcoming Socket created
serverPort = 8080   # Port 

serverSocket.bind(('', serverPort)) # Socket binding - to server address and port
serverSocket.listen(1) # Ensures we have 1 connection at a time

# server is running and listening 
while True:
    print("Server is Ready!")
    connectionSocket, addr = serverSocket.accept()
    try:
        msg = connectionSocket.recv(1024) # recieves request from client
        filename = msg.split()[1] # we need part of the HTTP header which we identify by using [1]
        data = open(filename[1:]) # read in the path including the '/' character that was extracted
        output = data.read() # store content in a buffer

        # Send the HTTP response header line to connection socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        connectionSocket.send(output.encode())

    # if exception occurs in try block the block below executes depending on whether it is IO or Index issue
    except IOError:
        print("Error - 404, File not Found!") 
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("404 Not Found".encode()) # sends this message to the connection socket - displayed on the browswer

    except IndexError:
        continue  
# close connection and server socket
connectionSocket.close()
serverSocket.close()