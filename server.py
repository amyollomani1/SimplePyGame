import socket
from _thread import *
import sys

server = "192.168.1.163" #use ipconfig getifaddr en0 command. This program only works for machines on local server
port = 5555 #this port is typically open

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2) #only 2 connections
print("Waiting for a connection, Server Started")

#holds position of players
pos = [(0,0),(100,100)]

def read_pos(str): 
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def threaded_client(conn, player):
    #conn.send(str.encode("Connected"))
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    
    while True:
        try:
            #data = conn.recv(2048) #ammount of bits to reciev
            #reply = data.decode("utf-8")
            
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data
            
            if not data: #if theres no more data being sent
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                    
                print("Recieved: ", data)
                print("Sending: ",reply)
                
            conn.sendall(str.encode(make_pos(reply))) #encode to bytes code for security purposes since server is public
        
        except:
            break
        
    print("Lost connection")
    conn.close()
    
currentPlayer = 0
            
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    
    start_new_thread(threaded_client, (conn,currentPlayer))
    currentPlayer +=1