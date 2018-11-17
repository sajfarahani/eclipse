import json

def json_message(direction):
    data = {}
    data['instruction'] = 'direction'
    print("data %s" % data)
    json_data = json.dumps(data)
    return json_data
