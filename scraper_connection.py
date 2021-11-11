import socket


def connect_to_scraper(msg_size, msg):
    socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 5050
    socket_connection.connect(('localhost', port))

    socket_connection.send(msg_size)
    socket_connection.send(msg)

    response_len = socket_connection.recv(64).decode('utf-8')
    if response_len:
        response_len = int(response_len)

        # Closing connection
        response = socket_connection.recv(response_len).decode('utf-8')
        close = '/q'.encode('utf-8')
        close_len = len(close)
        close_len = str(close_len).encode('utf-8')
        close_len += b' ' * (64 - len(close_len))
        socket_connection.send(close_len)
        socket_connection.send(close)

        return response
    else:
        return None
