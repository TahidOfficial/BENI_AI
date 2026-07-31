import json

FILE = "memory.json"

def load_memory():
    with open(FILE, "r") as file:
        return json.load(file)

def save_memory(data):
    with open(FILE, "w") as file:
        json.dump(data, file , indent=4)
