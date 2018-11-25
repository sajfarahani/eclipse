import json
import socket
from flask import Flask

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8192         # The port used by the server
app = Flask(__name__)

def json_message(direction):

    local_ip = socket.gethostbyname(socket.gethostname())
    data = {
        'sender' : local_ip,
        'instruction' : direction
    }

    json_data = json.dumps(data, sort_keys=False, indent=2)
    print("data %s" % json_data)

    post_message(json_data + ";")

    return json_data


def post_message(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data.encode())
        data = s.recv(1024)
    print('Received', repr(data))


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/direction', methods = ['POST'])
def post_direction()


if __name__ == '__main__':
    app.run(debug=True)