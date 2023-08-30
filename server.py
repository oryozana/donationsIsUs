import socket
import threading
import Consts

class Server:
    server_host = None
    server_port = None
    clients = []

    def start_communication_with_client(self,client_info):
        client_msg = None
        while client_msg != Consts.CLIENT_DISCONNECTED_CODE:
            print((client_info[0].recv(1024)).decode())
            client_info[0].send(("hello").encode())

    def __init__(self, server_host, port):
        self.server_host = server_host
        self.server_port = port

    def run_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.server_host, self.server_port))
        print("socket binded to port", self.server_port)
        s.listen(5)
        print("socket is listening")

        while True:
            c, addr = s.accept()
            print('Connected to :', addr[0], ':', addr[1])
            client_info = (c,addr)
            self.clients.append(client_info)
            threading.Thread(target=self.start_communication_with_client, args=(client_info, )).start()

        s.close()
