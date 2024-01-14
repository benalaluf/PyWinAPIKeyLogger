import socket


class Server:
    def __init__(self, ip, port):
        self.sock = socket.socket()
        self.sock.bind((ip, port))

        self.current_sequence = list()



    def main(self):
        self.sock.listen()
        print("LISTENING")

        client_sock, _ = self.sock.accept()

        while True:
            key = client_sock.recv(1024)
            self.check_sequences(int(key.decode()))
            # print(chr(int(key.decode())))


    def check_sequence(self, key, expected_sequence,message):
        if len(self.current_sequence) >= len(expected_sequence):
            return False
        if key == expected_sequence[len(self.current_sequence)]:
            self.current_sequence.append(key)

            if self.current_sequence == expected_sequence:
                print(message)
                self.current_sequence.clear()
            return True

        return False

    def check_sequences(self, key):
        self.check_sequence(key,[72,69,76,76,79],"client typed: hello")
        self.check_sequence(key,[162,67,162,86],"stop copying!!!")



if __name__ == '__main__':
    sever = Server('127.0.0.1', 8080)
    sever.main()
