import socket
from cryptography.fernet import Fernet

# Ключ для шифрування
key = b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y='
cipher_suite = Fernet(key)

# Читання вмісту файлу і шифрування
with open('secret.txt', 'rb') as file:
    file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)

  # Збереження зашифрованих даних у файлі для перевірки
    with open('crypted_test.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
        print("Encrypted data saved to 'crypted_test.txt'.")

# Створення сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'  # Можна використовувати 127.0.0.1
port = 42424

client_socket.connect((host, port))
print("Connected to the server.")

# Відправлення зашифрованих даних
client_socket.send(encrypted_data)
print("Encrypted data sent.")

client_socket.close()
