# Import socket module
import socket


def Main():
    host = '127.0.0.1'
    port = 2005
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    while True:
        message = input("enter_name")
        s.send(message.encode())
        data = s.recv(1024)
        print('Received from the server :', str(data.decode('ascii')))

    # close the connection
    s.close()


if __name__ == '__main__':
    Main()
