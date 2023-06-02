import socket

class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "192.168.1.163"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
     
        
    def getPos(self):
        return self.pos    
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode() #when connect, send something to signal it
        except:
            print("Failed to connect")
            pass
        
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

