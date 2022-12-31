import json

def read_from_api_file(file, attribute):
    f = open(file)
    data = json.load(f)

    for i in data:
        if i == attribute: return data[i]