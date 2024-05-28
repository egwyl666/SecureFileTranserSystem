# Secure File Transfer System

This project is a simple demonstration of secure file transfer between a client and a server using Python. It utilizes socket programming for network communication and the cryptography library to encrypt and decrypt files securely.

## Features

- **Secure Transmission**: Uses Fernet encryption from the Cryptography library to ensure data is securely transmitted over the network.
- **Simplicity**: Simple implementation of client-server architecture using Python sockets.
- **Aesthetic Console Output**: Utilizes the PyStyle library to enhance the console output aesthetics on the server-side.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or newer
- pip (Python package installer)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/secure-file-transfer-system.git
   cd secure-file-transfer-system
    ```

2. **Install required packages:**

    ```python
    pip install -r requirements.txt
    ```

## Usage
### Server
Start the server by running the `server.py` script:

```python
python server.py
```
The client will connect to the server, encrypt a specified file (secret.txt), and send the encrypted data. The server will then decrypt the data and save it as received.txt.

## Configuration

+ Encryption Key: The encryption key is hardcoded for demonstration purposes. For production environments, it's advisable to manage keys securely, possibly using environment variables or a key management system.
+ Host and Port: Set the host and port in both the client and server scripts if you need to run this system in a different environment or over the internet.
  
## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to improve the functionality or documentation of this project.

## License
This project is licensed under the [MIT License](https://github.com/egwyl666/SecureFileTranserSystem?tab=MIT-1-ov-file) - see the LICENSE file for details.

## Acknowledgments

+ Thanks to the Python Cryptography and PyStyle libraries for making encryption and console styling easier and more accessible.

### Notes
- Adjust the repository URL to match your actual GitHub repository URL.
- If you have a license file, you can link to it by replacing `[LICENSE](LICENSE.md)` with the actual path to your license file in your repository.
- Ensure that any configuration information, especially sensitive data like encryption keys, is managed securely as suggested.
