import json

import socket
print ("IP %s" % socket.gethostbyname(socket.gethostname()))

def json_message(direction):
    data = {}
    data['instruction'] = direction
    json_data = json.dumps(data, sort_keys=False, indent=2)
    print("data %s" % json_data)
    return json_data
