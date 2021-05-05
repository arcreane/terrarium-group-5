import json

with open('data.json') as json_data:
    data_dict = json.load(json_data)
    #json_data.get("data")
    print(data_dict["data"])
