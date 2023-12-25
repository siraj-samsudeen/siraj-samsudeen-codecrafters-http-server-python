# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        connection, address = server_socket.accept()  # wait for client
        print("connection from", address)
        client_message = connection.recv(1024).decode()
        headers = client_message.splitlines()
        path = headers[0].split()[1]
        header_lines = []
        if path == '/':
            header_lines.append('HTTP/1.1 200 OK')
            header_lines.append("\r\n")
        elif path.startswith('/user-agent'):
            header_lines.append('HTTP/1.1 200 OK')
            header_lines.append('Content-Type: text/plain')
            for header in headers[1:]:
                user_agent_prefix = 'User-Agent: '
                if header.startswith(user_agent_prefix):
                    user_agent = header.removeprefix(user_agent_prefix).strip()
                    break
            header_lines.append(f'Content-Length: {len(user_agent.encode())}')
            header_lines.append("")
            header_lines.append(user_agent)
            print(f"{path=}, {user_agent=}")
            
        elif path.startswith('/echo/'):
            header_lines.append('HTTP/1.1 200 OK')
            header_lines.append('Content-Type: text/plain')
            echo_string = path.split('/echo/')[1]
            print(f"{path=}, {echo_string=}")
            header_lines.append(f'Content-Length: {len(echo_string.encode())}')
            header_lines.append("")
            header_lines.append(echo_string)
        else:
            header_lines.append('HTTP/1.1 404 Not Found')
            header_lines.append("\r\n")
        response = "\r\n".join(header_lines)
        print(f"{repr(response)=}")
        connection.sendall(response.encode())
        connection.close()


if __name__ == "__main__":
    main()
