import os
import platform
import socket

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
            print("[Socket] : Binding success")
        except:
            print("[Socket] : Binding failed")

    def accept(self):
        print("[Socket] : Waiting for connection")
        self.connect, self.client_address = self.sock.accept()

    def send(self, msg):
        if type(msg) == str:
            msg = msg.encode("utf-8")
        self.connect.send(self._appendSizeToMSG(msg))

    def receive(self):
        msgLen = self._getMessageLen()
        chunks = []
        bytesRecd = 0
        while bytesRecd < msgLen:
            chunk = self.connect.recv(min(msgLen - bytesRecd, 2048))
            print(chunk)
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytesRecd = bytesRecd + len(chunk)
        return b''.join(chunks)


    def close(self):
        self.sock.close()

    def _appendSizeToMSG(self, msg):
        if (len(msg).bit_length() + 7) // 8 < 3:
            return bytes([(len(msg).bit_length() + 7) // 8]) + len(msg).to_bytes((len(msg).bit_length() + 7) // 8, 'big') + msg
        else:
            raise RuntimeError("[Socket] : Over max message len")

    def _getMessageLen(self):
        msgDigit = int.from_bytes(self.connect.recv(2), byteorder='big')
        a=int.from_bytes(self.connect.recv(msgDigit), byteorder='big')
        print(a)
        return a




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
        self.sock.send(self._appendSizeToMSG(msg))

    def receive(self):
        msgLen = self._getMessageLen()
        chunks = []
        bytesRecd = 0
        while bytesRecd < msgLen:
            chunk = self.sock.recv(min(msgLen - bytesRecd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytesRecd = bytesRecd + len(chunk)
        return b''.join(chunks)

    def _appendSizeToMSG(self, msg):
        # if len(bytes([len(msg)])) < 255:
        #     return bytes([len(bytes([len(msg)]))]) + bytes([len(msg)]) + msg
        if (len(msg).bit_length() + 7) // 8 < 3:
            return bytes([(len(msg).bit_length() + 7) // 8]) + len(msg).to_bytes((len(msg).bit_length() + 7) // 8, 'big') + msg
        else:
            raise RuntimeError("[Socket] : Over max message len")

    def _getMessageLen(self):
        msgDigit = int.from_bytes(self.sock.recv(2), byteorder='big')
        return int.from_bytes(self.sock.recv(msgDigit), byteorder='big')


if __name__ == "__main__":
    import threading
    import time

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
        msg = b"echo!echo!echo!echo!echo!"
        print("[SC] : sending %s" % msg)
        sc.send(msg)
        print("[SC] : waiting to receive")
        msg = sc.receive()
        print("[SC] : Received %s" % msg)

    t = threading.Thread(target=temp_sc)
    t.start()
    temp_ss()


