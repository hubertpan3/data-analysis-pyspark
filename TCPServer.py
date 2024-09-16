import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    Test docstring
    """

    def handle(self):
        data = self.request.recv(4096)
        print(data.decode('utf-8'))
        self.request.sendall(bytes("bob", 'utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9090
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
