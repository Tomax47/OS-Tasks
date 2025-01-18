#!/usr/bin/python3

import socket
import sys
from datetime import datetime

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))

    server_socket.listen(5)
    print(f"Server listening on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
        client_socket.send(current_time.encode())

        client_socket.close()
        print(f"Connection with {addr} closed")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 timeserver.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_server(port)
