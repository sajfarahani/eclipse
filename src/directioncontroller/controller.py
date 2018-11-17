import json
import socket


# def get_ip_address():
#     local_ip = socket.gethostbyname(socket.gethostname())



def json_message(direction):

    # data = {}
    local_ip = socket.gethostbyname(socket.gethostname())
    data = {
        'sender' : local_ip,
        'instruction' : direction
    }

    json_data = json.dumps(data, sort_keys=False, indent=2)
    print("data %s" % json_data)
    return json_data
