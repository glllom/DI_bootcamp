import json
import os
users_path = os.path.dirname(__file__)+'/data/users.json'


def add_user(username, email, password):
    if "" in [username, email, password]:
        print("All fields must contain values.")
        return
    with open(users_path, 'r+') as f:
        try:
            users = json.load(f)
        except json.decoder.JSONDecodeError:
            users = []
        if username not in list(map(lambda user: user['username'], users)):
            users.append({'username': username, 'email': email, 'password': password, 'cart': []})
        else:
            print("This username already exists.")
            return
        f.seek(0)
        json.dump(users, f, indent=4)


def check_user(username):
    with open(users_path, 'r') as f:
        try:
            users = json.load(f)
        except json.decoder.JSONDecodeError:
            return False
        return username in list(map(lambda user: user['username'], users))


def check_password(username, password):
    with open(users_path, 'r') as f:
        try:
            users = json.load(f)
        except json.decoder.JSONDecodeError:
            return False
        return next((
                password == user['password']
                for user in users
                if username == user['username']),
                False,
                )


def update_cart(username, cart_item):
    with open(users_path, 'r+') as f:
        try:
            users = json.load(f)
        except json.decoder.JSONDecodeError:
            return
        f.truncate(0)
        for user in users:
            if user['username'] == username:
                user['cart'] = cart_item
                break
        f.seek(0)
        json.dump(users, f, indent=4)


def get_cart(username):
    with open(users_path, 'r') as f:
        try:
            users = json.load(f)
        except json.decoder.JSONDecodeError:
            return []
        for user in users:
            if user['username'] == username:
                return user['cart']
