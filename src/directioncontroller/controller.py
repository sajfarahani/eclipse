import json
import socket
from flask_restful import Resource, Api
from flask import Flask

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8192         # The port used by the server
app = Flask(__name__)
api = Api(app)

class Direction(Resource):
    def get(self, direction):
        local_ip = socket.gethostbyname(socket.gethostname())
        data = {
            'sender' : local_ip,
            'instruction' : direction
        }

        json_data = json.dumps(data, sort_keys=False, indent=2)
        print("data %s" % json_data)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(json_data.encode())
            data = s.recv(1024)
            s.close()
        print('Received', repr(data))
        return "received post"

api.add_resource(Direction, '/direction/<direction>')

if __name__ == '__main__':
    app.run(debug=True)