import socket
from cryptography.fernet import Fernet
from pystyle import *
import os

# Just got bored, spiced it up a bit
os.system("cls")

os.system(f"title of Server - MADE by: Egwyl666")

# Decryption key
key = b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y='
cipher_suite = Fernet(key)

# Creating a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'  # Can use 127.0.0.1
port = 42424
server_socket.bind((host, port))

# Just looking pretty
banner = '***Server is running***'

server_socket.listen(5)
print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
Write.Print(f"Server listening on {host}:{port}",
            Colors.blue_to_purple, interval=0.04)
print()

# Really, really pretty

while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established.")

    received_data = client_socket.recv(1024)
    print("Data received. Decrypting...")
    decrypted_data = cipher_suite.decrypt(received_data)

    with open('recieved.txt', 'wb') as f:
        f.write(decrypted_data)
        print("Data decrypted and saved to 'recieved.txt'.")

    client_socket.close()
    break  # Closing the connection after receiving one set of data
