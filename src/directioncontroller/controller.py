import json

def json_message(direction):
    data = {}
    data['instruction'] = 'direction'
    json_data = json.dumps(direction, sort_keys=False, indent=2)
    print("data %s" % data)
    return json_data
