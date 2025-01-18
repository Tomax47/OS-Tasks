#!/usr/bin/python3

import socket
import sys

def connect_to_server(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))

    data = client_socket.recv(1024).decode()

    print(f"Received from server: {data}")

    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 timeclient.py <server_ip> <port>")
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])
    connect_to_server(ip, port)
