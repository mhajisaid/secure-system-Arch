import socket
import pwinput

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1233)

# Connect to the server
client_socket.connect(server_address)


def token_authentication(client_socket):
    # Receive and print the token prompt
    token_prompt = client_socket.recv(1024).decode('utf-8')
    print(token_prompt, end=' ')

    # Send the token
    token = input()
    client_socket.sendall(token.encode('utf-8'))

    # Receive and print the final response
    final_response = client_socket.recv(1024).decode('utf-8')
    print(final_response)

    if "successful" in final_response:
        print("Welcome! You have been authenticated successfully.")
        return True
    else:
        return False



try:
    for attempt in range(3):  # Allow only 3 attempts
        # Receive and print the first message (username prompt)
        username_prompt = client_socket.recv(1024).decode('utf-8')
        print(username_prompt, end=' ')

        # Send the username
        username = input()
        client_socket.sendall(username.encode('utf-8'))

        # Receive and print the second message (password prompt)
        password_prompt = client_socket.recv(1024).decode('utf-8')
        

        # Prompt user for password and display it as astiks 
        password = pwinput.pwinput(prompt=password_prompt)
        client_socket.sendall(password.encode('utf-8'))

        # Receive and print the response
        response = client_socket.recv(1024).decode('utf-8')
        print(response)

        if "successful" in response:
            # Authenticate with token only after a successful login
            if token_authentication(client_socket):
                # Do not break the loop; you can add further logic here if needed
                pass   
            
                     
    else:
        print("Maximum number of login attempts reached. Exiting.")

    
            
finally:
    # Clean up the connection
    client_socket.close()