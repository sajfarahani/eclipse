import json

def json_message(direction):
    data = {}
    data['instruction'] = 'direction'
    json_data = json.dumps(data)
    return json_data
