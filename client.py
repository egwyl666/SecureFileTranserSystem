import socket
from cryptography.fernet import Fernet

# Encryption key
key = b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y='
cipher_suite = Fernet(key)

# Reading file content and encrypting
with open('secret.txt', 'rb') as file:
    file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)

    # Saving encrypted data in a file for verification
    with open('crypted_test.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
        print("Encrypted data saved to 'crypted_test.txt'.")

# Creating a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'  # Can use 127.0.0.1
port = 42424

client_socket.connect((host, port))
print("Connected to the server.")

# Sending encrypted data
client_socket.send(encrypted_data)
print("Encrypted data sent.")

client_socket.close()
