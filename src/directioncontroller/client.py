import socket


def client_socket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(8192)

    print('Received', repr(data))


if __name__ == '__main__':
    client_socket()
