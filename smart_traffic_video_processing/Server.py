import socket

class SocketServer:
    def __init__(self):
        self.host = 'localhost'  # Use 'localhost' or '127.0.0.1' for local testing
        self.port = 50007
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.sock.bind((self.host, self.port))
            self.sock.listen(1)
            print(f"Server listening on {self.host}:{self.port}...")
            self.conn, self.addr = self.sock.accept()
            print(f"Connection established with {self.addr}")
        except socket.error as e:
            print(f"Error binding to port {self.port}: {e}")
            self.close()

    def send(self, data):
        try:
            self.conn.send(data.encode())
        except Exception as e:
            print(f"Error sending data: {e}")

    def receive(self):
        try:
            data = self.conn.recv(1024)  # Receive up to 1024 bytes
            if data:
                return data.decode()
            else:
                return None
        except Exception as e:
            print(f"Error receiving data: {e}")
            return None

    def close(self):
        try:
            self.conn.close()
            self.sock.close()
            print("Server socket closed.")
        except Exception as e:
            print(f"Error closing socket: {e}")

