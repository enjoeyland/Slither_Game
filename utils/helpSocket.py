import os
import platform
import socket

# from utils.setting import MSG_LEN


class SocketClient:
    def __init__(self, sock = None):
        if sock is None:
            if platform.system() == "Windows":
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            elif platform.system() == "Linux":
                self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, server_address): # Windows : (host, port), Linux : (server_address)
        self.sock.connect(server_address)

    def send(self, msg):
        if type(msg) == str:
            msg = msg.encode("utf-8")
        self.sock.send(msg)

    def receive(self, msg_len=0):
        # chunks = []
        # bytes_recd = 0
        # while bytes_recd < msg_len:
        #     chunk = self.sock.recv(min(msg_len - bytes_recd, 2048))
        #     if chunk == b'':
        #         raise RuntimeError("socket connection broken")
        #     chunks.append(chunk)
        #     bytes_recd = bytes_recd + len(chunk)
        # return b''.join(chunks)
        return self.sock.recv(2048)

class SocketServerForOneClient:
    def __init__(self, server_address, sock = None):
        if sock is None:
            if platform.system() == "Windows":
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            elif platform.system() == "Linux":
                try:
                    os.unlink(server_address)
                except OSError as e:
                    if os.path.exists(server_address):
                        print(e)
                self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        else:
            self.sock = sock

        try:
            self.sock.bind(server_address)
            self.sock.listen(1)
        except:
            print("[Socket] : Binding failed")

    def accept(self):
        print("[Socket] : Waiting for connection")
        self.connect, self.client_address = self.sock.accept()

    def send(self, msg):
        if type(msg) == str:
            msg = msg.encode("utf-8")
        self.connect.send(msg)

    def receive(self, msg_len =0):
        # chunks = []
        # bytes_recd = 0
        # while bytes_recd < msg_len:
        #     chunk = self.connect.recv(min(msg_len - bytes_recd, 2048))
        #     if chunk == b'':
        #         raise RuntimeError("socket connection broken")
        #     chunks.append(chunk)
        #     bytes_recd = bytes_recd + len(chunk)
        # return b''.join(chunks)
        return self.sock.recv(2048)

    def close(self):
        self.sock.close()

if __name__ == "__main__":
    import threading
    import time
    # pid = os.fork()
    def temp_ss():
        ss = SocketServerForOneClient(('localhost',3490))
        print("[SS] : socket server created")
        ss.accept()
        msg = ss.receive()
        print("[SS] : Recived %s" % msg)
        ss.send(msg)
    def temp_sc():
        sc = SocketClient()
        print("[SC] : socket client created")
        time.sleep(2)

        print("[SC] : connecting...")
        sc.connect(('localhost',3490))
        print("[SC] : connected")
        print("[SC] : sending")
        sc.send(b"echo")
        print("[SC] : waiting to receive")
        msg = sc.receive()
        print("[SC] : received %s" % msg)
    t = threading.Thread(target=temp_sc)
    t.start()
    temp_ss()


