def create_socket(port_number):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', port_number))
    server_socket.listen(1)

    return server_socket

socket_list = []

for port_number in range(1025,65536):
    try:
        socket_list.append(create_socket(port_number))
    except Exception: 
        pass 
