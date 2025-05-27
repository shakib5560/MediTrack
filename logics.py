import json

def read_json(patients: str):
    with open(patients, 'r') as file:
        content = file.read().strip()
        if not content:
            return {"message": "JSON file is empty."}
        data = json.loads(content)
        return data if data else {"message": "No data found in the JSON file."}