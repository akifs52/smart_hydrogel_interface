import json
import os

DATA_FILE = "user_data.json"

def load_users():
    if not os.path.exists(DATA_FILE):
        return {"patients": [], "doctors": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_user(user_type, user_data):
    data = load_users()
    if user_type == "patient":
        data["patients"].append(user_data)
    elif user_type == "doctor":
        data["doctors"].append(user_data)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def find_user(email, password, user_type):
    data = load_users()
    user_list = data["doctors"] if user_type == "doctor" else data["patients"]
    for user in user_list:
        if user.get("email") == email and user.get("password") == password:
            return user
    return None
