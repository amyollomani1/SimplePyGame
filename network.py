import socket
import pickle 

class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "192.168.1.163"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
     
        
    def getP(self):
        return self.p
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048)) #when connect, send something to signal it
        except:
            print("Failed to connect")
            pass
        
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data)) #sends string
            return pickle.loads(self.client.recv(2048)) #recieves object so use pickle
        except socket.error as e:
            print(e)


