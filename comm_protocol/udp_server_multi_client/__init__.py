import threading

from .udp_server import UDPServer


class UDPServerMultiClient(UDPServer):
    """Simple UDP Server for handling multiple clients"""
    def __init__(self, host, port, buff_size, handler, description=None):
        super().__init__(host, port, buff_size, None, description)
        self.handler = handler  # Handler function
        self.socket_lock = threading.Lock()

    def wait_for_client(self):
        """Wait for clients and handle their requests in a new thread"""
        try:
            while True:
                try:
                    data, client_address = self.sock.recvfrom(self.buff_size)
                    data = data.decode("utf-8")  # convert byte object to string
                    # start new thread and pass the data received the client_address and the socket itself
                    c_thread = threading.Thread(target=self.handler, args=(data, client_address, self.sock))
                    c_thread.daemon = True
                    c_thread.start()
                except OSError as err:
                    self.printwt(err)
        except KeyboardInterrupt:
            self.shutdown_server()
