import socket
from _thread import *
import sys
from player import Player
import pickle

server = "192.168.1.163" #use ipconfig getifaddr en0 command. This program only works for machines on local server
port = 5555 #this port is typically open

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen() 
print("Waiting for a connection, Server Started")



#holds position of players
players = [Player(0,0,50,50,(250,0,0)), Player(100,100,50,50,(0,0,255))]


def threaded_client(conn, player):
    
    #conn.send(str.encode("Connected"))
    conn.send(pickle.dumps(players[player]))
    reply = ""
    
    while True:
        try:
            #data = conn.recv(2048) #ammount of bits to reciev
            #reply = data.decode("utf-8")
            
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            
            if not data: #if theres no more data being sent
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                    
                print("Recieved: ", data)
                print("Sending: ",reply)
                
            conn.sendall(pickle.dumps(reply)) #encode to bytes code for security purposes since server is public
        
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