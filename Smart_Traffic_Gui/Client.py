import socket
import sys
import errno

class SocketClient:
    def __init__(self):
        self.host = 'localhost'  # Use 'localhost' or '127.0.0.1' if running locally
        self.port = 50007
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.sock.connect((self.host, self.port))
            self.sock.setblocking(False)  # Set socket to non-blocking mode
            print(f"Connected to server at {self.host}:{self.port}")
        except socket.error as e:
            print(f"Error connecting to server: {e}")
            sys.exit(1)

    def read(self):
        try:
            data = self.sock.recv(16)  # Receive up to 16 bytes
            if data:
                return data.decode()  # Decode the byte data to string
            else:
                return None  # No data received
        except socket.error as e:
            err = e.args[0]
            if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                return ""  # No data available
            else:
                # A "real" error occurred
                print(f"Socket error: {e}")
                sys.exit(1)

    def send(self, data):
        try:
            self.sock.send(data.encode())  # Encode the data to bytes before sending
        except socket.error as e:
            print(f"Error sending data: {e}")

    def close(self):
        try:
            self.sock.close()
            print("Socket connection closed.")
        except socket.error as e:
            print(f"Error closing socket: {e}")
