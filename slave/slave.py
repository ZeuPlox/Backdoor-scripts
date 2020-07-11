#!/usr/bin/env python
#_*_ coding utf8 _*_

import os
import socket

s = socket.socket() #socket instance
port = 8080 
host = input(str("Please enter the server address: ")) #asking for the server that the user want to connect
s.connect((host, port)) #connect to the server
print("\nConnected to the server successfully")

#Connection has been completed 

#Command receiving and execution

while True:
    command = s.recv(1024) #receive the command from server script for execution
    command = command.decode() #decode command
    print("\nCommand received") 
    if command == "getcwd":
        directory = str(os.getcwd()) #get actual directory        
        files = str(os.listdir(directory)) #get files for the actual directory
        s.send(directory.encode()) #send the info encoded to server script
        s.send(files.encode())
        print("\nCommand has been executed successfully...")

    elif command == "custom_dir":
        try:
            userInput = s.recv(5000) #receive instruction
            userInput = userInput.decode()
            files = str(os.listdir(userInput)) #get files of the directory
            s.send(files.encode())
            print("\nCommand has been executed succesfully...")
        except Exception as e:
            error = str("Path not found, try again")
            s.send(error.encode())
            print("\nError has been sent")

    elif command == 'download_file':
        try:
            userInput = s.recv(5000) #receive the instruccion
            userInput = userInput.decode()
            file = open(userInput, 'rb') #open the file especified as readable file
            fileName = str(os.path.basename(file.name)) #get name of the file with extension
            s.send(fileName.encode()) #send file name
            data = file.read() #copy info to data var
            s.send(data) #send info
            print("\nFile has been sent successfully")
        except Exception as e:
            print("error try again")                        

    else:
        print("\nCommand not recognised")