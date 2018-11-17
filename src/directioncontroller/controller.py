import json
import socket


def json_message(direction):

    local_ip = socket.gethostbyname(socket.gethostname())
    data = {
        'sender' : local_ip,
        'instruction' : direction
    }

    json_data = json.dumps(data, sort_keys=False, indent=2)
    print("data %s" % json_data)
    return json_data


