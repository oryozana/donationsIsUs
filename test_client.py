# Import socket module
import socket

import Consts


def Main():
    host = '10.56.145.166'
    # Define the port on which you want to connect
    port = 2005

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host, port))

    # message you send to server

    while True:
        code = input(f"Enter code\n1. get user stat code\n999. exit")
        s.send(code.encode())  # send code to server
        if code == Consts.GET_USER_STAT_CODE:
            # send data of wanted person
            msg_to_server = input("enter user details")
            s.send(msg_to_server.encode())
            msg_from_server = s.recv(1024).decode()
            print(msg_from_server)

    s.close()


if __name__ == '__main__':
    Main()
