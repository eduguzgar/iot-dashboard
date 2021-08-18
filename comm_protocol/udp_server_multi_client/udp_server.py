import socket
from datetime import datetime


class UDPServer:
    """Simple UDP Server"""

    def __init__(self, host, port, buff_size, handler, description=None):
        self.host = host  # Host address
        self.port = port  # Host port
        self.buff_size = buff_size  # Buffer size
        self.handler = handler  # Handler function
        self.description = description  # Socket description
        self.sock = None  # Socket

    def printwt(self, msg):
        """Print message with current date and time"""
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_date_time}] {msg}", flush=True)

    def configure_server(self):
        """Configure the server"""

        # create UDP socket with IPv4 addressing
        self.printwt("Creating " + self.description + " socket...")

        # bind server to the address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.printwt(f"Binding server to {self.host}:{self.port}...")
        self.sock.bind((self.host, self.port))
        self.printwt(f"Server binded to {self.host}:{self.port}")

    def wait_for_client(self):
        """Wait for a client"""

        while True:
            try:
                data, client_address = self.sock.recvfrom(self.buff_size)

                data = data.decode("utf-8")  # convert byte object to string

                self.handler(data)
            except OSError as err:
                self.printwt(err)

    def shutdown_server(self):
        """Shutdown the UDP server"""
        self.printwt("Shutting down " + self.description + " server...")
        self.sock.close()
