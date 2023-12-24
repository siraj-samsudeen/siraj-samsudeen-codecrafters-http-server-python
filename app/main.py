# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    connection, address = server_socket.accept()  # wait for client
    print("connection from", address)
    client_message = connection.recv(1024).decode()
    line1 = client_message.splitlines()[0]
    path = line1.split()[1]
    if path == '/':
        response = 'HTTP/1.1 200 OK\r\n\r\n'
    else:
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
    connection.send(response.encode())
    connection.close()


if __name__ == "__main__":
    main()
