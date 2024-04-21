import socket
import ssl


class Client:

    def __init__(self, link: str):
        link = link.split('/')
        if link[0][0:5] == 'https':
            port = 443
        else:
            port = 80

        self.resp = b''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (link[2], port)
        self.sock.connect(self.addr)

    def get(self):
        request = f'GET / HTTP/1.1\r\nHost: {self.addr[0]}\r\n'

        console_input = ''
        while console_input != 'end':
            console_input = str(input())
            request += console_input + '\r\n'
        request += '\r\n'

        if self.addr[1] == 443:
            cnt = ssl.create_default_context()
            with cnt.wrap_socket(self.sock,
                                 server_hostname=self.addr[0]) as wrp:
                wrp.sendall(request.encode())
                while True:
                    answer = wrp.recv(1024)
                    if not answer:
                        break
                    self.resp += answer

        else:
            self.sock.sendall(request.encode())
            while True:
                answer = self.sock.recv(1024)
                if not answer:
                    break
                self.resp += answer

        if self.resp:
            print(self.resp.decode())
        else:
            print('Response timed out')

    def head(self):
        request = f'HEAD / HTTP/1.1\r\nHost: {self.addr[0]}\r\n'

        console_input = ''
        while console_input != 'end':
            console_input = str(input())
            request += console_input + '\r\n'
        request += '\r\n'

        if self.addr[1] == 443:
            cnt = ssl.create_default_context()
            with cnt.wrap_socket(self.sock,
                                 server_hostname=self.addr[0]) as wrp:
                wrp.sendall(request.encode())
                while True:
                    answer = wrp.recv(1024)
                    if not answer:
                        break
                    self.resp += answer

        else:
            self.sock.sendall(request.encode())
            while True:
                answer = self.sock.recv(1024)
                if not answer:
                    break
                self.resp += answer

        if self.resp:
            print(self.resp.decode())
        else:
            print('Response timed out')

    def post(self):
        request = f'POST / HTTP/1.1\r\nHost: {self.addr[0]}\r\n'

        console_input = ''
        while console_input != 'end':
            console_input = str(input())
            request += console_input + '\r\n'
        request += '\r\n'

        if self.addr[1] == 443:
            cnt = ssl.create_default_context()
            with cnt.wrap_socket(self.sock,
                                 server_hostname=self.addr[0]) as wrp:
                wrp.sendall(request.encode())
                while True:
                    answer = wrp.recv(1024)
                    if not answer:
                        break
                    self.resp += answer

        else:
            self.sock.sendall(request.encode())
            while True:
                answer = self.sock.recv(1024)
                if not answer:
                    break
                self.resp += answer

        if self.resp:
            print(len(self.resp.decode()))
        else:
            print('Response timed out')

    def save_output(self):
        file = open('output.txt', 'w')
        file.write(self.resp.decode())
        file.close()
