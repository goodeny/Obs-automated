import json

def insert_message_json():
        with open("data.json", "r") as f:
            data = json.load(f)
        
        data['message'] = 'custom message inserted'
        with open("data.json", "w") as file:
            json.dump(data, file, indent= 6)

insert_message_json()