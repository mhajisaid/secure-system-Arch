import socket
import random
import string

# Create Socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Define the server address and port 
server_address = ('localhost' , 1233)

# Bind the socket to the address and port
server_socket.bind(server_address)

# Listen for incoming connection
server_socket.listen(5)

# Usernames and passwords 
credentials = {
    'mohammed': 'pass123',
    'hajisaid': 'home123',
    'hassan': 'toy123'
}

# Maximum number of login attempts
max_tries = 3

# Function to generate a random token
def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=3))

# Function to authenticate a client using a token
def authenticate_with_token(connection, username):
    token = generate_token()
    connection.sendall(f"Token: {token}\nEnter the token: ".encode('utf-8'))
    entered_token = connection.recv(1024).decode('utf-8').strip()

    if entered_token == token:
        connection.sendall(b"Login successful!")
        print(f'User {username} authenticated correctly.')
        return True
    else:
        connection.sendall(b"Invalid token! Please try again.")
        return False

# Client login simulation 
def handle_client(connection):
    tries = 0
    remaining_attempts = max_tries
    
    while tries < max_tries:
        # Request username
        connection.send(str.encode('ENTER USERNAME : '))
        username = connection.recv(1024).decode('utf-8').strip()

        # Request password
        connection.send(str.encode('ENTER PASSWORD : '))
        password = connection.recv(1024).decode('utf-8').strip()

        # Verify credentials
        if username in credentials and credentials[username] == password:
            connection.send(str.encode("Login successful!"))

            # Authenticate with token
            if authenticate_with_token(connection, username):
                return True
            else:
                tries += 1
                remaining_attempts = max_tries - tries
        else:
            connection.sendall(f"Invalid credentials! Remaining attempts: {remaining_attempts}".encode('utf-8'))
            tries += 1
            remaining_attempts = max_tries - tries

    connection.sendall(b"Too many unsuccessful attempts. You are locked out.")
    print(f'User {username} locked out due to too many unsuccessful attempts.')
    return False

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    connection, client_address = server_socket.accept()
    print('Connection from', client_address)

    try:
        if not handle_client(connection):
            # Lock out the client
            pass
        pass

    finally:
        # Clean up the connection
        connection.close()